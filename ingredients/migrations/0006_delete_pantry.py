# Generated by Django 5.0.7 on 2024-09-24 10:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("ingredients", "0005_pantry"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Pantry",
        ),
    ]
