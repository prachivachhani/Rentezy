# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-25 19:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team6', '0022_auto_20180225_1843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='car_pic',
            field=models.ImageField(default=b'static/pic_folder/', upload_to=b'static/pic_folder/'),
        ),
    ]
