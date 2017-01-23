from django.test import TestCase, Client, RequestFactory
from django.contrib.auth.models import User
from imager_images.models import Album, Photo, PUBLISHED
import factory
import random

# Create your tests here.


class PhotoFactory(factory.django.DjangoModelFactory):
    """Creates Photo models for testing."""

    class Meta:
        """Assign Photo model as product of factory."""

        model = Photo

    title = factory.Faker('sentence')
    description = factory.Faker('text')
    published = random.choice(PUBLISHED)
    owner = factory.SubFactory(factory.Sequence(lambda n: "The Chosen {}".format(n)))
    img_file = factory.django.ImageField()


class AlbumFactory(factory.django.DjangoModelFactory):
    """Creates Album models for testing."""

    class Meta:
        """Assign Album model as product of factory."""

        model = Album

    title = factory.Faker('sentence')
    description = factory.Faker('text')
    published = random.choice(PUBLISHED)
    owner = factory.SubFactory(factory.Sequence(lambda n: "The Chosen {}".format(n)))


class PhotoTestCase(TestCase):
    """Testing the Photo model."""

    def setUp(self):
        self.photos = [PhotoFactory.create() for i in range(20)]

    def test_profile_is_made_when_user_is_saved(self):
        """Photo should be created."""
        self.assertTrue(Photo.objects.count() == 20)


class AlbumTestCase(TestCase):
    """Testing the Photo model."""

    def setUp(self):
        self.albums = [AlbumFactory.create() for i in range(20)]

    def test_profile_is_made_when_user_is_saved(self):
        """Album should be created."""
        self.assertTrue(Album.objects.count() == 20)
