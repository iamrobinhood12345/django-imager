"""View module for our DJANGO REST TUTORIAL."""
from django.contrib.auth.models import User
from rest_framework import generics, permissions
from imager_profile.models import ImagerProfile
from imager_images.models import Photo, Album
from imager_api.permissions import IsOwnerOrReadOnly
from imager_api.serializers import PhotoSerializer, AlbumSerializer, UserSerializer
from rest_framework import renderers, viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view, detail_route
from rest_framework.reverse import reverse


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """Viewset automatically provides `list` and `detail` actions."""
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PhotoViewSet(viewsets.ModelViewSet):
    """New Snippet View Set.

    Viewset automatically provides `list`, `create`, `retrieve`, `update`
    and `destroy` actions. Additionally we also provide an extra `highlight`
    action.
    """

    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class AlbumViewSet(viewsets.ModelViewSet):
    """New Snippet View Set.

    Viewset automatically provides `list`, `create`, `retrieve`, `update`
    and `destroy` actions. Additionally we also provide an extra `highlight`
    action.
    """

    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)