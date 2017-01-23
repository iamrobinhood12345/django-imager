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