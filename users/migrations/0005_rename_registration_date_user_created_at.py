# Generated by Django 4.2.16 on 2024-09-27 17:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0004_user_registration_date"),
    ]

    operations = [
        migrations.RenameField(
            model_name="user",
            old_name="registration_date",
            new_name="created_at",
        ),
    ]
