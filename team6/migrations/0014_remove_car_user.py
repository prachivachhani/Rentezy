# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-25 00:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('team6', '0013_auto_20180225_0022'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='user',
        ),
    ]
