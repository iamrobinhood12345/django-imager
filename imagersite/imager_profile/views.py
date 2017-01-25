from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from imager_profile.models import ImagerProfile
from imager_images.models import Photo


def profile(request, username):
    user = ImagerProfile.objects.get(user_id=1)
    photos = Photo.objects.filter(user_id=user.user_id)
    return render(request, 'profile.html',
            {'username': username,
             'photos': photos})
