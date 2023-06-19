# Generated by Django 4.1.5 on 2023-06-17 18:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0003_likepost_alter_post_created_at"),
    ]

    operations = [
        migrations.RenameField(
            model_name="likepost", old_name="user_name", new_name="username",
        ),
        migrations.AlterField(
            model_name="post",
            name="created_at",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 6, 17, 18, 5, 4, 216354)
            ),
        ),
    ]