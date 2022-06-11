from django.apps import AppConfig


class WritersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'writers'

    def ready(self):
        import writers.signals
