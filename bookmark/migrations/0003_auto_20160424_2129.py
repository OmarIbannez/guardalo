# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-24 21:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bookmark", "0002_auto_20160424_2123"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bookmark", name="image", field=models.URLField(),
        ),
    ]
