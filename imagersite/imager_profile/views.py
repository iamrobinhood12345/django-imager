from django.shortcuts import render
from django.contrib.auth.models import User
from imager_images.models import Photo
from django.conf import settings
from django.views.generic import TemplateView


class ProfileView(TemplateView):
    """Return the Profile View inheriting from TemplateView."""

    template_name = 'imager_profile/profile.html'

    def get_context_data(self, username=None):
        """Get profiles and return them."""
        if self.request.user.is_authenticated():
            public_images = self.request.user.profile.photo.filter(published='public').count()
            private_images = self.request.user.profile.photo.filter(published='private').count()
            profile = self.request.user.profile
            return {'profile': profile,
                    'public_images': public_images,
                    'private_images': private_images}
        else:
            error_message = "You're not signed in."
            return {'error': error_message}


class OtherUserProfileView(TemplateView):
    """Return other user profile views."""

    template_name = 'imager_profile/profile.html'

    def get_context_data(self, username):
        """View for other users profile's."""
        user = User.objects.get(username=username)
        profile = user.profile
        public_images = profile.photo.filter(published='public').count()
        private_images = profile.photo.filter(published='private').count()
        return {'profile': profile,
                'public_images': public_images,
                'private_images': private_images}
