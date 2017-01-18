# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-17 02:20
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ImagerProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_camera', models.CharField(choices=[('Nikon', 'Nikon'), ('Canon', 'Canon'), ('Instagram', 'Instagram'), ('Mobile', 'Mobile'), ('SONY', 'SONY')], default='', max_length=35)),
                ('type_photography', models.CharField(choices=[('Nature', 'Nature'), ('SpecialEventWedding', 'Special Event/Wedding'), ('CityScape', 'CityScape'), ('BabyPics', 'Baby Pics'), ('Sexting', 'Sexting'), ('Celebrity', 'Celebrity'), ('DomesticatedAnimals', 'Domesticated Animals')], default='', max_length=35)),
                ('employable', models.BooleanField(default=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('bio', models.CharField(blank=True, max_length=800, null=True)),
                ('personal_website', models.URLField(blank=True, null=True)),
                ('phone_number', models.CharField(max_length=12)),
                ('travel_radius', models.IntegerField()),
                ('is_active', models.BooleanField(default=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
            managers=[
                ('active', django.db.models.manager.Manager()),
            ],
        ),
    ]