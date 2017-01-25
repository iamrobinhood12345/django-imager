from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime


def profile(request, username):
    user = User.objects.get(username=username)
    photos = Photo.objects.filter(user=user)
    return render(request, 'profile.html',
            {'username': username,
             'photos': photos})
