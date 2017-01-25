from django.conf.urls import url
from django.conf import settings
from . import views

urlpattern = [
    url(r'^user/(\w+)/$', views.profile, name='profile'),
]
