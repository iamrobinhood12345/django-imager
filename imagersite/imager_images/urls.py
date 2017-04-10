from django.conf.urls import url
from imager_images.views import (
    PhotoView,
    LibraryView,
    AlbumView,
    SinglePhotoView,
    SingleAlbumView,
    AddPhotoView,
    AddAlbumView,
    EditSinglePhotoView,
    EditSingleAlbumView,
)

urlpatterns = [
    url(r'^library/$', LibraryView.as_view(), name='library'),
    url(r'^photos$', PhotoView.as_view(), name='allphotos'),
    url(r'^photos/(?P<photoid>\d+)/$', SinglePhotoView.as_view(),
        name='singlephoto'),
    url(r'^albums$', AlbumView.as_view(), name='album'),
    url(r'^albums/(?P<albumid>\d+)/$', SingleAlbumView.as_view(),
        name='singlealbum'),
    url(r'^photos/add/$', AddPhotoView.as_view(), name='add_photo'),
    url(r'^albums/add/$', AddAlbumView.as_view(), name='add_album'),
    url(r'^albums/(?P<pk>\d+)/edit/$', EditSingleAlbumView.as_view(),
        name='edit_album'),
    url(r'^photos/(?P<pk>\d+)/edit/$', EditSinglePhotoView.as_view(),
        name='edit_photo'),
]
