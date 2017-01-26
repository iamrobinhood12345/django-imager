from django.conf.urls import url
from . import views
from imager_images.views import (
    PhotoView,
    LibraryView,
)

urlpatterns = [
    url(r'^post_url/$', PhotoView.as_view(), name='post_photo'),
    url(r'^library/$', LibraryView.as_view(), name='library'),
    # url(r'(?P<albumid>\d+)/$', views.album_view, name='album'),
    url(r'^$', PhotoView.as_view(), name='photo'),
]
