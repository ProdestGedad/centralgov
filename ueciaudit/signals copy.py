import json
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.forms.models import model_to_dict
from crum import get_current_user

from .models import (
    Norma, Procedimento, Auditoria,
    ChecklistItem, NaoConformidade, AuditLog
)

def registra_log(instance, operacao):
    usuario = get_current_user()
    if usuario and usuario.is_anonymous:
        usuario = None

    # para C/U, gravar campos atuais
    detalhes = model_to_dict(instance) if operacao in ('C','U') else {}
    AuditLog.objects.create(
        operacao   = operacao,
        usuario    = usuario,
        modelo     = instance.__class__.__name__,
        objeto_id  = instance.pk,
        detalhes   = detalhes
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
