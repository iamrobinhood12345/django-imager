from django.db import models
from imager_profile.models import ImagerProfile
from django.utils import timezone
from datetime import datetime



class Photo(models.Model):
    user_id = models.ForeignKey(ImagerProfile)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    date_uploaded = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)
    date_published = models.DateTimeField()
    PUBLISHED = [
        (1, 'Private'),
        (2, 'Shared'),
        (3, 'Public')
    ]
    published = models.SmallIntegerField(
        choices = PUBLISHED,
        default = 1
    )
    image = models.ImageField(upload_to='images')

class Album(models.Model):
    user_id = models.ForeignKey(ImagerProfile)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    date_uploaded = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    date_published = models.DateTimeField()
    PUBLISHED = [
        (1, 'Private'),
        (2, 'Shared'),
        (3, 'Public')
    ]
    published = models.SmallIntegerField(
        choices = PUBLISHED,
        default = 1
    )
    cover = models.ImageField(upload_to='images')
