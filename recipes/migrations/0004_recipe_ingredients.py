# Generated by Django 5.0.7 on 2024-09-23 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("recipes", "0003_remove_recipe_ingredients"),
    ]

    operations = [
        migrations.AddField(
            model_name="recipe",
            name="ingredients",
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
