# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-19 01:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0007_message_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='staff',
            field=models.BooleanField(default=False),
        ),
    ]
