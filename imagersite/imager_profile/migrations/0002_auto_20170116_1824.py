# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-17 02:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imager_profile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagerprofile',
            name='phone_number',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='imagerprofile',
            name='travel_radius',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='imagerprofile',
            name='type_camera',
            field=models.CharField(blank=True, choices=[('Nikon', 'Nikon'), ('Canon', 'Canon'), ('Instagram', 'Instagram'), ('Mobile', 'Mobile'), ('SONY', 'SONY')], default='', max_length=35, null=True),
        ),
        migrations.AlterField(
            model_name='imagerprofile',
            name='type_photography',
            field=models.CharField(blank=True, choices=[('Nature', 'Nature'), ('SpecialEventWedding', 'Special Event/Wedding'), ('CityScape', 'CityScape'), ('BabyPics', 'Baby Pics'), ('Sexting', 'Sexting'), ('Celebrity', 'Celebrity'), ('DomesticatedAnimals', 'Domesticated Animals')], default='', max_length=35, null=True),
        ),
    ]