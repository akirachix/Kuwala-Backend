# from .apps import recipe

# default_app_config = 'recipe.apps.RecipeConfig'

from django.apps import AppConfig

class RecipeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'recipe'