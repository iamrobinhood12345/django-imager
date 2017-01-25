from django.conf.urls import url
from imager_profile.views import profile_view, other_user_profile_view


urlpatterns = [
    url(r'^$', profile_view, name="profile"),
    url(r'^(?P<username>\w+)/$', other_user_profile_view, name="user_profile")
]
