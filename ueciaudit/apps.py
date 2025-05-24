from django.apps import AppConfig


class UeciauditConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ueciaudit'

    def ready(self):
        import ueciaudit.signals