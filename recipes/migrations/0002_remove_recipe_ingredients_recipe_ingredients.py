# Generated by Django 4.2.16 on 2024-09-23 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ingredients", "0004_remove_ingredients_category_ingredients_categories"),
        ("recipes", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="recipe",
            name="ingredients",
        ),
        migrations.AddField(
            model_name="recipe",
            name="ingredients",
            field=models.ManyToManyField(to="ingredients.ingredients"),
        ),
    ]
