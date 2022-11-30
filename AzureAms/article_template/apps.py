from django.apps import AppConfig
from django.core.signals import request_finished



class article_templateConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'article_template'

    # def ready(self):
    #     from . import signals
        
    #     request_finished.connect(signals.reorder)