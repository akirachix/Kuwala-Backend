from django.db import models
from django.core.exceptions import ValidationError

class Ingredients(models.Model):
    ingredients_id = models.AutoField(primary_key=True)
    ingredients_name = models.CharField(max_length=20)
    quantity = models.IntegerField()

    def clean(self):
        if self.quantity < 0:
            raise ValidationError('Quantity cannot be negative.')

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.ingredients_id} {self.ingredients_name}"


# Create your models here.
