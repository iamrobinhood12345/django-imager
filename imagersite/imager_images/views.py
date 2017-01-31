from django.shortcuts import render
from django.http.response import HttpResponseForbidden, HttpResponseNotFound
from django.views.generic import ListView, CreateView, UpdateView
from .forms import PhotoForm, AlbumForm, EditPhotoForm, EditAlbumForm
from imager_profile.models import ImagerProfile
from imager_images.models import Photo, Album
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.utils import timezone
from django.urls import reverse_lazy


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

    model = Photo
    template_name = 'photos.html'

    def get_context_data(self):
        photos = Photo.objects.all()
        return {'photos': photos}


class SinglePhotoView(ListView):
    """View a single photo on a page."""
    model = Photo
    template_name = 'single_photo.html'

    def get_context_data(self):
        photo = Photo.objects.filter(id=int(self.kwargs['photoid'])).first()
        if photo and photo.owner:
            if photo.owner.user.username == self.request.user.username:
                return {'photo': photo}
        else:
            return HttpResponseForbidden()


class AlbumView(ListView):
    """Return the AlbumView inheriting from ListView."""
    model = Album
    template_name = 'library.html'

    def get_context_data(self):
        """Get albums and return them."""
        albums = Album.objects.all()
        return {'albums': albums}


class SingleAlbumView(ListView):
    """Return the AlbumView inheriting from ListView."""
    model = Album
    template_name = 'single_album.html'

    def get_context_data(self):
        """Get albums and return them."""
        album = Album.objects.get(id=int(self.kwargs['albumid']))
        if album.owner.user.username == self.request.user.username or album.published == 'public':
            return {'album': album}
        else:
            return HttpResponseNotFound()


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


class EditSingleAlbumView(LoginRequiredMixin, UpdateView):
    """Edit an album."""

    login_required = True
    success_url = reverse_lazy('library')
    template_name = 'edit_album.html'
    model = Album
    form_class = EditAlbumForm

    def get_form(self):
        """Retrieve form and customize some fields."""
        form = super(EditSingleAlbumView, self).get_form()
        form.fields['cover_image'].queryset = self.request.user.profile.photo.all()
        # form.fields['images'].queryset = self.request.user.profile.photo.all()
        return form

    def user_is_user(self, request):
        """Test if album's owner is current user."""
        if request.user.is_authenticated():
            self.object = self.get_object()
            return self.object.owner.user == request.user
        return False

    def dispatch(self, request, *args, **kwargs):
        """If user owns album let them do stuff."""
        if not self.user_is_user(request):
            return HttpResponseForbidden()
        return super(EditSingleAlbumView, self).dispatch(
            request, *args, **kwargs)


class EditSinglePhotoView(LoginRequiredMixin, UpdateView):
    """Edit a photo."""

    login_required = True
    success_url = reverse_lazy('library')
    template_name = 'edit_photo.html'
    model = Photo
    form_class = EditPhotoForm
    form_class.Meta.exclude.append('photo')

    def user_is_user(self, request):
        """Test if album's owner is current user."""
        if request.user.is_authenticated():
            self.object = self.get_object()
            return self.object.owner.user == request.user
        return False

    def dispatch(self, request, *args, **kwargs):
        """If user doesn't own album, raise 403, else continue."""
        if not self.user_is_user(request):
            return HttpResponseForbidden()
        return super(EditSinglePhotoView, self).dispatch(
            request, *args, **kwargs)
