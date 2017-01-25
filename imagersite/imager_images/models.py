"""Models for imager_images module. Contains Photo and Album model Classes."""

from django.db import models
from django.utils import timezone
from imager_profile.models import ImagerProfile

PUBLISHED = [
    ('private', 'Private'),
    ('shared', 'Shared'),
    ('public', 'Public')
]


class Photo(models.Model):
    """The Photo class."""

    user_id = models.ForeignKey(ImagerProfile,
                                related_name="photo",
                                blank=True,
                                null=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    date_uploaded = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)
    date_published = models.DateTimeField(
        default=timezone.now,
        blank=True,
        null=True
    )
    published = models.CharField(
        max_length=100000,
        choices=PUBLISHED,
        default='private'
    )
    image_file = models.ImageField(upload_to='images')

    def __str__(self):
        """Return title as string."""
        return self.title


class Album(models.Model):
    """The Album class."""

    user_id = models.ForeignKey(ImagerProfile,
                                related_name="album",
                                blank=True,
                                null=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    date_uploaded = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    date_published = models.DateTimeField(
        default=timezone.now,
        blank=True,
        null=True)
    published = models.CharField(
        max_length=100000,
        choices=PUBLISHED,
        default='private'
    )

    images = models.ManyToManyField(
        "Photo",
        related_name="albums_of_photos",
        symmetrical=False)

    cover_image = models.ImageField(upload_to='images/cover_photos')

    def __str__(self):
        """Return title as string."""
        return self.title
