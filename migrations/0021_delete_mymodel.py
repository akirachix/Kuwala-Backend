# Generated by Django 5.0.7 on 2024-09-22 10:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0020_alter_mymodel_created_at'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MyModel',
        ),
    ]
