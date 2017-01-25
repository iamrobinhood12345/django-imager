from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^post_url/$', views.post_photo, name='post_photo'),
]
