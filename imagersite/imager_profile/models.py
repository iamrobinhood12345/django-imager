from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

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

class ActiveProfileManager(models.Manager):
    """Query ImagerProfile of active user."""

    def get_querysets(self):
        """Return query set of profiles for active users."""
        query = super(ActiveProfileManager, self).get_querysets()
        return query.filter(user['is_active']=True)


class ImagerProfile(models.Model)
    user = models.OneToOneField(
        User,
        related_name="profile",
        on_delete=models.CASCADE
    )
    type_camera = models.CharField(default='', max_length=35, choices=CAMERA_TYPES)
    type_photography = models.CharField(default='', max_length=35, choices=PHOTOGRAPHY_TYPES)
    employable = models.BooleanField(default=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    bio = models.CharField(max_length=800, blank=True, null=True)
    personal_website = models.URLField(blank=True, null=True)
    phone_number = models.CharField(max_length=12)
    travel_radius = models.IntegerField()
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )


    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def make_user_profile(sender, instance, **kwargs):
    """Instantiate a PatronProfile, connect to a new User instance, save that profile."""
    new_profile = PatronProfile(user=instance)
    new_profile.money_owed = 0.00
    new_profile.save()



