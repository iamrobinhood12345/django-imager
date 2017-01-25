from django.conf.urls import url
from django.conf import settings
from imager_profile import views

urlpatterns = [
    url(r'^(?P<username>\w+)/$', views.profile, name='profile'),
]
