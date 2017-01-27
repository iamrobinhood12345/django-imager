from django.conf.urls import url
from . import views
from imager_images.views import (
    PhotoView,
    LibraryView,
    AlbumView,
)

urlpatterns = [
    url(r'^post_url/$', PhotoView.as_view(), name='post_photo'),
    url(r'^$', LibraryView.as_view(), name='library'),
    url(r'^$', PhotoView.as_view(), name='photo'),
    url(r'(?P<albumid>\d+)/$', AlbumView.as_view(), name='album'),
]
