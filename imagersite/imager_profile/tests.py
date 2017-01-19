"""Tests for the lender_profile app."""
from django.test import TestCase
from django.contrib.auth.models import User
from imager_profile.models import ImagerProfile
import factory


class ProfileTestCase(TestCase):
    """The Profile Model test runner."""

    class UserFactory(factory.django.DjangoModelFactory):
        class Meta:
            model = User

        username = factory.Sequence(lambda n: "The Chosen {}".format(n))
        email = factory.LazyAttribute(
            lambda x: "{}@foo.com".format(x.username.replace(" ", ""))
        )

    def setUp(self):
        """The appropriate setup for the appropriate test."""
        self.foo = "bar"
        self.users = [self.UserFactory.create() for i in range(20)]

    def test_profile_is_made_when_user_is_saved(self):
        """Imager Profile should be created when a User is saved."""
        self.assertTrue(ImagerProfile.objects.count() == 20)

    def test_profile_is_associated_with_actual_users(self):
        """Imager Profile should be attached to User."""
        profile = ImagerProfile.objects.first()
        self.assertTrue(hasattr(profile, "user"))
        self.assertIsInstance(profile.user, User)

    def test_user_has_profile_attached(self):
        """User should have a Imager Profile attached."""
        user = self.users[0]
        self.assertTrue(hasattr(user, "profile"))
        self.assertIsInstance(user.profile, ImagerProfile)

    def test_user_is_active(self):
        """User should be active."""
        user = self.users[0]
        self.assertTrue(user.is_active)
        self.assertTrue(user.profile.is_active)

    def test_str_method_on_imager_profile(self):
        """String method should return a string"""
        user = self.users[0]
        self.assertTrue(type(str(user.profile)), str)
        self.assertTrue(str(user.profile) == 'Username: The Chosen 40\n                  Camera: \n                  Photography Type: \n                  Employable?: True\n                  Address: None\n                  About Me: \n                  Website: None\n                  Phone: None\n                  Travel Radius: None')
