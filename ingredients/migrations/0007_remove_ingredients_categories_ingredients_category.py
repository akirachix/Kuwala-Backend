# Generated by Django 5.0.7 on 2024-09-24 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ingredients", "0006_delete_pantry"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="ingredients",
            name="categories",
        ),
        migrations.AddField(
            model_name="ingredients",
            name="category",
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
