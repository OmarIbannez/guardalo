# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-05-07 18:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookmark', '0008_auto_20160428_2259'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookmark',
            options={'ordering': ('-created_at',)},
        ),
    ]
