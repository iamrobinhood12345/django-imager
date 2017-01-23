from django.test import TestCase, Client, RequestFactory
from django.contrib.auth.models import User
from imager_profile.models import ImagerProfile
import factory

# Create your tests here.

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: "The Chosen {}".format(n))
    email = factory.LazyAttribute(
        lambda x: "{}@foo.com".format(x.username.replace(" ", ""))
    )


class ProfileTestCase(TestCase):
    """The Profile Model test runner."""

    def setUp(self):
        """The appropriate setup for the appropriate test."""
        self.users = [UserFactory.create() for i in range(20)]

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
        """String method should return a string."""
        user = self.users[0]
        self.assertTrue(type(str(user.profile)), str)
        self.assertTrue(str(user.profile) == 'Username: {}\n                  Camera: \n                  Photography Type: \n                  Employable?: True\n                  Address: None\n                  About Me: \n                  Website: None\n                  Phone: None\n                  Travel Radius: None'.format(user.username))

    def test_inactive_users(self):
        """Test that inactive users are not active."""
        the_user = self.users[0]
        the_user.is_active = False
        the_user.save()
        self.assertTrue(ImagerProfile.active.count() == User.objects.count() - 1)

    def test_delete_user_deletes_profile(self):
        """Deleting a user should delete a profile associated with it."""
        user = self.users[0]
        self.assertTrue(ImagerProfile.objects.count() == 20)
        count = ImagerProfile.objects.count()
        user.delete()
        self.assertTrue(ImagerProfile.objects.count() == count - 1)

    def test_delete_user_deletes_user(self):
        """Deleting a user should delete the user."""
        user = self.users[0]
        count = User.objects.count()
        user.delete()
        self.assertTrue(User.objects.count() == count - 1)