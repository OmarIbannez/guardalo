# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-24 21:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookmark', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmark',
            name='image',
            field=models.ImageField(max_length=255, upload_to=b''),
        ),
    ]
