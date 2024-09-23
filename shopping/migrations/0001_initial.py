# Generated by Django 4.2.16 on 2024-09-23 12:18

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ShoppingList",
            fields=[
                (
                    "shopping_list_id",
                    models.AutoField(primary_key=True, serialize=False),
                ),
                ("shopping_list_name", models.CharField(max_length=255)),
                (
                    "date_created",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ShoppingListItem",
            fields=[
                (
                    "shopping_list_item_id",
                    models.AutoField(primary_key=True, serialize=False),
                ),
                ("item", models.CharField(default="item", max_length=255)),
                ("quantity", models.IntegerField()),
                ("unit", models.CharField(max_length=100)),
                (
                    "shopping_list",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="shopping.shoppinglist",
                    ),
                ),
            ],
        ),
    ]
