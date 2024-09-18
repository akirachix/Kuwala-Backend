# Generated by Django 5.1.1 on 2024-09-09 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe_id', models.PositiveSmallIntegerField()),
                ('title', models.CharField(max_length=255)),
                ('ingredients', models.TextField()),
                ('instructions', models.TextField()),
                ('servings', models.IntegerField()),
                ('cooking_time', models.IntegerField()),
                ('category', models.PositiveSmallIntegerField()),
            ],
        ),
    ]
