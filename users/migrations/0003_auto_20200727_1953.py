# Generated by Django 3.0.7 on 2020-07-27 19:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20180623_0107'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='middle_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='photo',
        ),
    ]
