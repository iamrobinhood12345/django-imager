# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-25 07:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imager_images', '0009_auto_20170123_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='image_file',
            field=models.ImageField(upload_to='images'),
        ),
    ]
