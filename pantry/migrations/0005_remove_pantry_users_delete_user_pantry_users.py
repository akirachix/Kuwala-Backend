# Generated by Django 5.0.7 on 2024-09-19 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pantry', '0004_pantry_users'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pantry',
            name='users',
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AddField(
            model_name='pantry',
            name='users',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
    ]
