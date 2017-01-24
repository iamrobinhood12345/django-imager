from django.test import TestCase, Client, RequestFactory
from django.contrib.auth.models import User
from imager_profile.models import ImagerProfile
from imager_images.models import Album, Photo, PUBLISHED
import factory
import random
# Create your tests here.


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: "The Chosen {}".format(n))
    email = factory.LazyAttribute(
        lambda x: "{}@foo.com".format(x.username.replace(" ", ""))
    )


class PhotoFactory(factory.django.DjangoModelFactory):
    """Creates Photo models for testing."""

    class Meta:
        """Assign Photo model as product of factory."""

        model = Photo

    title = factory.Faker('sentence')
    description = factory.Faker('text')
    published = random.choice(PUBLISHED)[1]
    image_file = factory.django.ImageField()
    user_id = random.choice(ImagerProfile.objects.all())


class AlbumFactory(factory.django.DjangoModelFactory):
    """Creates Album models for testing."""

    class Meta:
        """Assign Album model as product of factory."""

        model = Album

    title = factory.Faker('sentence')
    description = factory.Faker('text')
    published = random.choice(PUBLISHED)[1]
    cover_image = factory.django.ImageField()


class PhotoTestCase(TestCase):
    """Testing the Photo model."""

    def setUp(self):
        self.users = [UserFactory.create() for i in range(20)]
        self.photos = [PhotoFactory.create() for i in range(20)]

    def test_photo_is_made(self):
        """Photo should be created."""
        self.assertTrue(Photo.objects.count() == 20)


class AlbumTestCase(TestCase):
    """Testing the Photo model."""

    def setUp(self):
        self.users = [UserFactory.create() for i in range(20)]
        self.albums = [AlbumFactory.create() for i in range(20)]

    def test_album_is_made(self):
        """Album should be created."""
        self.assertTrue(Album.objects.count() == 20)
