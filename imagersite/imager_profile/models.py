from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import uuid

CAMERA_TYPES = (
    ('Nikon', 'Nikon'),
    ('Canon', 'Canon'),
    ('Instagram', 'Instagram'),
    ('Mobile', 'Mobile'),
    ('SONY', 'SONY')
)

PHOTOGRAPHY_TYPES = (
    ('Nature', 'Nature'),
    ('SpecialEventWedding', 'Special Event/Wedding'),
    ('CityScape', 'CityScape'),
    ('BabyPics', 'Baby Pics'),
    ('Sexting', 'Sexting'),
    ('Celebrity', 'Celebrity'),
    ('DomesticatedAnimals', 'Domesticated Animals')
)


class ActiveUserManager(models.Manager):
    """Query ImagerProfile of active user."""

    def get_queryset(self):
        """Return query set of profiles for active users."""
        query = super(ActiveUserManager, self).get_queryset()
        return query.filter(user__is_active__exact=True)


class ImagerProfile(models.Model):
    user = models.OneToOneField(
        User,
        related_name="profile",
        on_delete=models.CASCADE
    )
    type_camera = models.CharField(default='', max_length=35, choices=CAMERA_TYPES, blank=True, null=True)
    type_photography = models.CharField(default='', max_length=35, choices=PHOTOGRAPHY_TYPES, blank=True, null=True)
    employable = models.BooleanField(default=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    bio = models.TextField(default="")
    personal_website = models.URLField(blank=True, null=True)
    phone_number = models.CharField(max_length=12, blank=True, null=True)
    travel_radius = models.IntegerField(blank=True, null=True)
    imager_id = models.UUIDField(default=uuid.uuid4, editable=False)
    active = ActiveUserManager()
    objects = models.Manager()

    def __str__(self):
        return """Username: {Username}
                  Camera: {Camera}
                  Photography Type: {PhotographyType}
                  Employable?: {Employable}
                  Address: {Address}
                  About Me: {AboutMe}
                  Website: {Website}
                  Phone: {Phone}
                  Travel Radius: {TravelRadius}""".format(
            Username=self.user.username,
            Camera=self.type_camera,
            PhotographyType=self.type_photography,
            Employable=self.employable,
            Address=self.address,
            AboutMe=self.bio,
            Website=self. personal_website,
            Phone=self.phone_number,
            TravelRadius=self.travel_radius)

    @property
    def is_active(self):
        return self.user.is_active


@receiver(post_save, sender=User)
def make_user_profile(sender, instance, **kwargs):
    """Instantiate a PatronProfile, connect to a new User instance, save that profile."""

    if kwargs["created"]:
        new_profile = ImagerProfile(user=instance)
        new_profile.save()
