
from django.db import models

class Recipe(models.Model):
    recipe_id = models.CharField(max_length=255, primary_key=True)
    title = models.CharField(max_length=255)
    ingredients = models.JSONField(default=list)  
    instructions = models.TextField()
    image_url = models.URLField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return f"{self.title}"

