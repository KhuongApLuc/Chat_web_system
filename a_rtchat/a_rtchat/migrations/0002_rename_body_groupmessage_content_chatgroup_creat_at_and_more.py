# Generated by Django 5.0.8 on 2024-08-22 04:23

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("a_rtchat", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameField(
            model_name="groupmessage",
            old_name="body",
            new_name="content",
        ),
        migrations.AddField(
            model_name="chatgroup",
            name="creat_at",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="chatgroup",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name="groupmessage",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False, unique=True),
        ),
        migrations.CreateModel(
            name="Blocks",
            fields=[
                (
                    "id",
                    models.IntegerField(primary_key=True, serialize=False, unique=True),
                ),
                ("blocked_at", models.DateTimeField(auto_now_add=True)),
                (
                    "blocked",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="blocked_by",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "blocker",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="blocked_user",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Participants",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("join_at", models.DateTimeField(auto_now_add=True)),
                ("role", models.CharField(max_length=50)),
                ("active", models.BooleanField(default=True)),
                (
                    "chatgroup",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="a_rtchat.chatgroup",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Receiption",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("content", models.TextField()),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="sent_receptions",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "chatgroup",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="a_rtchat.chatgroup",
                    ),
                ),
                (
                    "message_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="a_rtchat.groupmessage",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
