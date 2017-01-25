from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from .forms import PhotoForm

def post_photo(request):
    form = PhotoForm(request.POST, request.FILES)
    if form.is_valid():
        photo = form.save(commit=False)
        photo.user=request.user
        photo.save()
        # form.save(commit = True)
        #below code was before refactoring to use a meta class in forms
            # photo = Photo(
            #         name = form.cleaned_data['title'],
            #         description = form.cleaned_data['description'],
            #         )
            # photo.save()
    #after adding a photo, return to Index or Home
    return HttpResponseRedirect('/')

def photos(request):
    photos = Photo.objects.all()
    form = PhotoForm()
    return render(request, 'photos.html',
                    {'photos': photos, 'form': form})
