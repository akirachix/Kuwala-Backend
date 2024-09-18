

from django.db import models

class Recipe(models.Model):
    # recipe_id=models.PositiveSmallIntegerField()
    title = models.CharField(max_length=255)
    ingredients = models.TextField()
    instructions = models.TextField()
    servings = models.IntegerField()  
    cooking_time = models.IntegerField() 
    # ingredients_id= models.PositiveSmallIntegerField()

    def __str__(self):
        return f"{self.title} {self.ingredients} {self.instructions}"

    