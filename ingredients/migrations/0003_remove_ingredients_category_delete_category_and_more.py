# Generated by Django 5.0.7 on 2024-09-19 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ingredients', '0002_category_ingredients_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingredients',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.AddField(
            model_name='ingredients',
            name='category',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
    ]
