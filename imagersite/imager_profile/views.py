from django.shortcuts import render
from django.contrib.auth.models import User
from imager_images.models import Photo
from django.conf import settings


def profile_view(request):
    """View for the user's own profile."""
    if request.user.is_authenticated():
        public_images = request.user.profile.photo.filter(published='public').count()
        private_images = request.user.profile.photo.filter(published='private').count()
        profile = request.user.profile
        return render(request, "imager_profile/profile.html",
                               {'profile': profile,
                                'public_images': public_images,
                                'private_images': private_images
                                })
    else:
        error_message = "You're not signed in."
        return render(request, "imager_profile/profile.html",
                               {'error': error_message
                                })


def other_user_profile_view(request, username):
    """View for other user's profile."""
    user = User.objects.get(username=username)
    profile = user.profile
    public_images = profile.photo.filter(published='public').count()
    private_images = profile.photo.filter(published='private').count()
    return render(request, "imager_profile/profile.html",
                           {'profile': profile,
                            'public_images': public_images,
                            'private_images': private_images
                            })