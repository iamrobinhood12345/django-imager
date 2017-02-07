"""Web API to provide a way of serializing and deserializing the snippet instances into representations such as json."""

from rest_framework import serializers
from imager_images.models import Photo, Album
from django.contrib.auth.models import User


class PhotoSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(
        view_name='photo-highlight', format='html')

    class Meta:
        model = Photo
        fields = (
            'owner',
            'id',
            'title',
            'description',
            'date_uploaded',
            'date_modified',
            'date_published',
            'published',
            'image_file',
            'tags')


class AlbumSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(
        view_name='album-highlight', format='html')

    class Meta:
        model = Album
        fields = (
            'owner',
            'id',
            'title',
            'description',
            'date_uploaded',
            'date_modified',
            'date_published',
            'published',
            'images',
            'tags',
            'cover_image')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(
        many=True, view_name='user-detail', read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'photos', 'albums')