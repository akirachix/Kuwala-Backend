# Generated by Django 5.1.1 on 2024-09-18 11:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pantry', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pantry',
            old_name='pantry_item_id',
            new_name='id',
        ),
    ]
