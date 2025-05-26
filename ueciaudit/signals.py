from datetime import date, datetime
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.forms.models import model_to_dict
from django.db.models.fields.files import FieldFile
from crum import get_current_user

from .models import (
    Norma, Procedimento, Auditoria,
    ChecklistItem, NaoConformidade, AuditLog
)

def registra_log(instance, operacao):
    usuario = get_current_user()
    if usuario and usuario.is_anonymous:
        usuario = None

    detalhes = {}
    if operacao in ('C', 'U'):
        raw = model_to_dict(instance)
        for key, val in raw.items():
            # Datas → ISO strings
            if isinstance(val, (date, datetime)):
                detalhes[key] = val.isoformat()
            # Arquivos → nome do arquivo (path relativo)
            elif isinstance(val, FieldFile):
                detalhes[key] = val.name or ''
            # Qualquer outro valor serializável
            else:
                detalhes[key] = val

    AuditLog.objects.create(
        operacao  = operacao,
        usuario   = usuario,
        modelo    = instance.__class__.__name__,
        objeto_id = instance.pk,
        detalhes  = detalhes
    )

MODELS = [Norma, Procedimento, Auditoria, ChecklistItem, NaoConformidade]

@receiver(post_save)
def on_save(sender, instance, created, **kwargs):
    if sender in MODELS:
        registra_log(instance, 'C' if created else 'U')

@receiver(post_delete)
def on_delete(sender, instance, **kwargs):
    if sender in MODELS:
        registra_log(instance, 'D')
