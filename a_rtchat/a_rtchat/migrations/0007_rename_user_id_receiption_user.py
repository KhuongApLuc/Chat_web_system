# Generated by Django 5.0.8 on 2024-08-26 09:32

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("a_rtchat", "0006_rename_user_receiption_user_id"),
    ]

    operations = [
        migrations.RenameField(
            model_name="receiption",
            old_name="user_id",
            new_name="user",
        ),
    ]
