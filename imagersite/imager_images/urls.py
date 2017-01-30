from django.conf.urls import url
from . import views
from imager_images.views import (
    PhotoView,
    LibraryView,
    AlbumView,
    SinglePhotoView,
    SingleAlbumView,
)

urlpatterns = [
    url(r'^post_url/$', PhotoView.as_view(), name='post_photo'),
    url(r'^library/$', LibraryView.as_view(), name='library'),
    url(r'^photos$', PhotoView.as_view(), name='allphotos'),
    url(r'^photos/(?P<photoid>\d+)/$', SinglePhotoView.as_view(), name='photo'),
    url(r'^albums$', AlbumView.as_view(), name='album'),
    url(r'^albums/(?P<albumid>\d+)/$', SingleAlbumView.as_view(), name='album'),
]
