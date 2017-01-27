from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, TemplateView
from datetime import datetime
from .forms import PhotoForm
from imager_profile.models import ImagerProfile
from imager_images.models import Photo, Album


class LibraryView(ListView):
    """"Return the libraryView inheriting from ListView."""

    template_name = 'library.html'

    def get_context_data(self):
        """Get albums and photos and return them."""
        profile = ImagerProfile.active.get(user__username=self.request.user.username)
        photos = profile.photo.all()
        albums = profile.album.all()
        username = self.request.user.username
        return {'photos': photos, 'profile': profile, 'albums': albums, 'username': username}

    def get_queryset(self):
        """."""
        return {}


class PhotoView(ListView):

    def post(self, request):
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.user = request.user
            photo.save()
        # form.save(commit = True)
        #below code was before refactoring to use a meta class in forms
            # photo = Photo(
            #         name = form.cleaned_data['title'],
            #         description = form.cleaned_data['description'],
            #         )
            # photo.save()
        #after adding a photo, return to Index or Home
        return render(request, 'photos.html', {'form': form})

    def get(self, request):
        photos = Photo.objects.all()
        form = PhotoForm()
        return render(request, 'photos.html',
                      {'photos': photos, 'form': form})


class AlbumView(ListView):
    """Return the AlbumView inheriting from ListView."""
    # template_name = 'imager_images/templates/album.html'
    model = Album

    def get_context_data(self):
        """Get albums and return them."""
        album = Album.objects.get(id=self.kwargs['albumid'])
        # album = Album.objects.get()
        if album.published == 'public' or album.owner == self.request.user.user_id:
            photos = album.images.all
            return {'album': album, 'photos': photos}
        else:
            return HttpResponseForbidden()
