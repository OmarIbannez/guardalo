# Generated by Django 3.0.7 on 2020-08-21 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bookmark", "0011_auto_20200727_1953"),
    ]

    operations = [
        migrations.AddField(
            model_name="bookmark",
            name="connection_error",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="bookmark",
            name="fetched",
            field=models.BooleanField(default=False),
        ),
    ]
