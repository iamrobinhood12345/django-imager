from django.conf.urls import url
from imager_profile.views import (
    ProfileView,
    OtherUserProfileView
)


urlpatterns = [
    url(r'^$', ProfileView.as_view(), name="profile"),
    url(r'^(?P<username>\w+)/$', OtherUserProfileView.as_view(), name="user_profile")
]
