# # Generated by Django 4.2.16 on 2024-09-27 16:14

# from django.db import migrations, models


# class Migration(migrations.Migration):

#     dependencies = [
#         ("users", "0003_alter_user_options"),
#     ]

#     operations = [
#         migrations.AddField(
#             model_name="user",
#             name="registration_date",
#             field=models.DateTimeField(auto_now_add=True, default=1),
#             preserve_default=False,
#         ),
#     ]


from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_alter_user_options"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="registration_date",
            field=models.DateTimeField(auto_now_add=True),
            preserve_default=False,
        ),
    ]