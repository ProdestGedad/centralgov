from django.conf import settings
from types import SimpleNamespace

def global_settings(request):
    config = SimpleNamespace(
        footer_1     = settings.FOOTER_1,
        footer_2     = settings.FOOTER_2,
        footer_3     = settings.FOOTER_3,
        nome_sistema = settings.NOME_SISTEMA,
        hue_rotation = settings.HUE_ROTATION,
    )
    return {
        'global': SimpleNamespace(
            config  = config,
            version = settings.APP_VERSION,
            # você também pode incluir outros campos, ex:
            # nome_cidadao   = request.user.get_full_name(),
            # impersonated   = getattr(request, 'impersonated_user', None),
        )
    }
