from random import randint
from django.shortcuts import render
from imager_images.models import Photo
from django.conf import settings


def home_page(request, *args, **kwargs):
    photos = Photo.objects.all()
    if photos:
        idx = randint(0, photos.count() - 1)
        random_picture = photos[idx]
        img_url = random_picture.image_file.url
    else:
        img_url = ''
    context = {'img_url': img_url}
    return render(request, 'home.html', context)
