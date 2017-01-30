from django.shortcuts import render
from django.http import HttpResponse, HttpResponseForbidden
from django.views.generic import ListView, TemplateView, CreateView
from datetime import datetime
from .forms import PhotoForm, AlbumForm
from imager_profile.models import ImagerProfile
from imager_images.models import Photo, Album

from django.shortcuts import redirect
from django.utils import timezone


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


class SinglePhotoView(ListView):
    """View a single photo on a page."""
    model = Photo
    template_name = 'single_photo.html'

    def get_context_data(self):
        photo = Photo.objects.filter(id=int(self.kwargs['photoid'])).first()
        # import pdb; pdb.set_trace()
        return {'photo': photo}


class AlbumView(ListView):
    """Return the AlbumView inheriting from ListView."""
    # template_name = 'imager_images/templates/album.html'
    model = Album
    template_name = 'library.html'

    def get_context_data(self):
        """Get albums and return them."""
        albums = Album.objects.all()
        return {'albums': albums}


class SingleAlbumView(ListView):
    """Return the AlbumView inheriting from ListView."""
    model = Album
    template_name = 'library.html'

    def get_context_data(self):
        """Get albums and return them."""
        albums = Album.objects.get(id=int(self.kwargs['albumid']))
        if albums.owner.user.username == self.request.user.username or albums.published == 'public':
            return {'albums': albums}


class AddPhotoView(CreateView):
    """Class based view for creating photos."""

    model = Photo
    form_class = PhotoForm
    template_name = 'add_photo.html'

    def form_valid(self, form):
        photo = form.save()
        photo.owner = self.request.user.profile
        photo.date_uploaded = timezone.now()
        photo.date_modified = timezone.now()
        if photo.published == "public":
            photo.published_date = timezone.now()
        photo.save()
        return redirect('library')


class AddAlbumView(CreateView):
    """Class based view for creating photos."""

    model = Album
    form_class = AlbumForm
    template_name = 'add_album.html'

    def form_valid(self, form):
        album = form.save()
        album.owner = self.request.user.profile
        album.date_uploaded = timezone.now()
        album.date_modified = timezone.now()
        if album.published == "public":
            album.published_date = timezone.now()
        album.save()
        return redirect('library')
