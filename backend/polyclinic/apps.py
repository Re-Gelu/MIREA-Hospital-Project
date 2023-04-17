from django.apps import AppConfig
from watson import search as watson


class PolyclinicConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'polyclinic'
    verbose_name = 'Магазин'
