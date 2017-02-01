from django.test import TestCase
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.files.uploadedfile import SimpleUploadedFile
from django.conf import settings
from django.urls import reverse_lazy

from imager_profile.models import ImagerProfile
from imager_images.models import Photo, Album

import factory
# Create your tests here.


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
    username = factory.Sequence(lambda n: "Imgr User {}".format(n))
    email = factory.LazyAttribute(
        lambda x: "{}@datsite.com".format(x.username.replace(" ", ""))
    )


class ImageFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Photo
    title = factory.Sequence(lambda n: "Image {}".format(n))
    image_file = SimpleUploadedFile(name='image_1.jpg', content=open('imagersite/static/images/image_1.jpg', 'rb').read(), content_type='image/jpeg')


class AlbumFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Album
    title = factory.Sequence(lambda n: "Album {}".format(n))
    cover_image = SimpleUploadedFile(name='image_1.jpg', content=open('imagersite/static/images/image_1.jpg', 'rb').read(), content_type='image/jpeg')
    description = "Calvin and hobbes album"


class ImageTestCase(TestCase):
    """The Image App Test Runner."""

    def setUp(self):
        """User setup for tests."""
        self.users = [UserFactory.create() for i in range(10)]
        self.photo = [ImageFactory.create() for i in range(10)]
        self.album = [AlbumFactory.create() for i in range(10)]

    def test_image_title(self):
        """Test that the image has a title."""
        self.assertTrue("Image" in Photo.objects.first().title)

    def test_image_has_description(self):
        """Test that the Image description field can be assigned."""
        image = Photo.objects.first()
        image.description = "This is a good image."
        image.save()
        self.assertTrue(Photo.objects.first().description == "This is a good image.")

    def test_image_has_published(self):
        """Test the image published field."""
        image = Photo.objects.first()
        image.published = 'public'
        image.save()
        self.assertTrue(Photo.objects.first().published == "public")

    def test_image_date_modified(self):
        """Test that the image has a date modified default."""
        image = Photo.objects.first()
        self.assertTrue(image.date_modified)

    def test_image_date_uploaded(self):
        """Test that the image has a date uploaded default."""
        image = Photo.objects.first()
        self.assertTrue(image.date_uploaded)

    def test_image_no_date_date_published(self):
        """Test that the image does not have a date published before assignment."""
        image = Photo.objects.first()
        self.assertFalse(image.date_published)

    def test_image_date_date_published(self):
        """Test that the image has a date published after assignment."""
        image = Photo.objects.first()
        image.date_published = timezone.now
        self.assertTrue(image.date_published)

    def test_image_has_no_owner(self):
        """Test that image has no owner."""
        image = Photo.objects.first()
        self.assertFalse(image.owner)

    def test_image_has_owner(self):
        """Test that image has an owner after assignment."""
        image = Photo.objects.first()
        user1 = User.objects.first()
        image.owner = user1.profile
        self.assertTrue(image.owner)

    def test_owner_has_image(self):
        """Test that the owner has the image."""
        image = Photo.objects.first()
        user1 = User.objects.first()
        image.owner = user1.profile
        image.save()
        self.assertTrue(user1.profile.photo.count() == 1)

    def test_two_images_have_owner(self):
        """Test two images have the same owner."""
        image1 = Photo.objects.all()[0]
        image2 = Photo.objects.all()[1]
        user1 = User.objects.first()
        image1.owner = user1.profile
        image2.owner = user1.profile
        image1.save()
        image2.save()
        self.assertTrue(image1.owner == user1.profile)
        self.assertTrue(image2.owner == user1.profile)

    def test_owner_has_two_images(self):
        """Test that owner has two image."""
        image1 = Photo.objects.all()[0]
        image2 = Photo.objects.all()[1]
        user1 = User.objects.first()
        image1.owner = user1.profile
        image2.owner = user1.profile
        image1.save()
        image2.save()
        self.assertTrue(user1.profile.photo.count() == 2)

    def test_image_has_no_album(self):
        """Test that the image is in an album."""
        image = Photo.objects.first()
        self.assertTrue(image.albums_of_photos.count() == 0)

    def test_image_has_album(self):
        """Test that the image is in an album."""
        image = Photo.objects.first()
        album1 = Album.objects.first()
        image.albums_of_photos.add(album1)
        self.assertTrue(image.albums_of_photos.count() == 1)

    def test_album_has_no_image(self):
        """Test that an album has no image before assignemnt."""
        album1 = Album.objects.first()
        self.assertTrue(album1.images.count() == 0)

    def test_album_has_image(self):
        """Test that an album has an image after assignemnt."""
        image = Photo.objects.first()
        album1 = Album.objects.first()
        image.albums_of_photos.add(album1)
        self.assertTrue(image.albums_of_photos.count() == 1)

    def test_two_images_have_album(self):
        """Test that two images have same album."""
        image1 = Photo.objects.all()[0]
        image2 = Photo.objects.all()[1]
        album1 = Album.objects.first()
        image1.albums_of_photos.add(album1)
        image2.albums_of_photos.add(album1)
        image1.save()
        image2.save()
        self.assertTrue(image1.albums_of_photos.all()[0] == album1)
        self.assertTrue(image2.albums_of_photos.all()[0] == album1)

    def test_album_has_two_images(self):
        image1 = Photo.objects.all()[0]
        image2 = Photo.objects.all()[1]
        album1 = Album.objects.first()
        image1.albums_of_photos.add(album1)
        image2.albums_of_photos.add(album1)
        image1.save()
        image2.save()
        self.assertTrue(album1.images.count() == 2)

    def test_image_has_two_albums(self):
        """Test that an image has two albums."""
        image1 = Photo.objects.first()
        album1 = Album.objects.all()[0]
        album2 = Album.objects.all()[1]
        image1.albums_of_photos.add(album1)
        image1.albums_of_photos.add(album2)
        image1.save()
        self.assertTrue(image1.albums_of_photos.count() == 2)

    def test_album_title(self):
        """Test that the album has a title."""
        self.assertTrue("Album" in Album.objects.first().title)

    def test_album_has_description(self):
        """Test that the album description field can be assigned."""
        album = Album.objects.first()
        album.description = "This is a good album."
        album.save()
        self.assertTrue(Album.objects.first().description == "This is a good album.")

    def test_album_has_published(self):
        """Test the album publisalbumhed field."""
        album = Album.objects.first()
        album.published = 'public'
        album.save()
        self.assertTrue(Album.objects.first().published == "public")

    def test_album_date_modified(self):
        """Test that the album has a date modified default."""
        album = Album.objects.first()
        self.assertTrue(album.date_modified)

    def test_album_date_created(self):
        """Test that the album has a date uploaded default."""
        album = Album.objects.first()
        self.assertTrue(album.date_uploaded)

    def test_album_no_date_date_published(self):
        """Test that the album does not have a date published before assignment."""
        album = Album.objects.first()
        self.assertFalse(album.date_published)

    def test_album_date_date_published(self):
        """Test that the album has a date published after assignment."""
        album = Album.objects.first()
        album.date_published = timezone.now
        self.assertTrue(album.date_published)

    def test_album_has_no_owner(self):
        """Test that album has no owner."""
        album = Album.objects.first()
        self.assertFalse(album.owner)

    def test_album_has_owner(self):
        """Test that album has an owner after assignment."""
        album = Album.objects.first()
        user1 = User.objects.first()
        album.owner = user1.profile
        self.assertTrue(album.owner)

    def test_owner_has_album(self):
        """Test that the owner has the album."""
        album = Album.objects.first()
        user1 = User.objects.first()
        album.owner = user1.profile
        album.save()
        # import pdb; pdb.set_trace()
        self.assertTrue(user1.profile.album.count() == 1)

    def test_two_albums_have_owner(self):
        """Test two albums have the same owner."""
        album1 = Album.objects.all()[0]
        album2 = Album.objects.all()[1]
        user1 = User.objects.first()
        album1.owner = user1.profile
        album2.owner = user1.profile
        album1.save()
        album2.save()
        self.assertTrue(album1.owner == user1.profile)
        self.assertTrue(album2.owner == user1.profile)

    def test_owner_has_two_albums(self):
        """Test that owner has two albums."""
        album1 = Album.objects.all()[0]
        album2 = Album.objects.all()[1]
        user1 = User.objects.first()
        album1.owner = user1.profile
        album2.owner = user1.profile
        album1.save()
        album2.save()
        self.assertTrue(user1.profile.album.count() == 2)

    def test_logged_in_user_has_library(self):
        """A logged in user has a library."""
        user = UserFactory.create()
        user.save()
        self.client.force_login(user)
        response = self.client.get(reverse_lazy("library"))
        self.assertTrue(response.status_code == 200)

    def test_logged_in_user_sees_their_albums(self):
        """Logged in user should see their albums."""
        user = UserFactory.create()
        album1 = Album.objects.first()
        album2 = Album.objects.all()[1]
        user.profile.album.add(album1)
        user.profile.album.add(album2)
        user.save()
        self.client.force_login(user)

        response = self.client.get(reverse_lazy("library"))
        self.assertTrue(album1.description in str(response.content))

    def test_photo_view(self):
        """Test images on photo view."""
        image1 = Photo.objects.all()[0]
        image2 = Photo.objects.all()[1]
        user1 = User.objects.first()
        image1.owner = user1.profile
        image2.owner = user1.profile
        image1.save()
        image2.save()
        self.client.force_login(user1)
        response = self.client.get(reverse_lazy("allphotos"))
        self.assertTrue(image1.image_file.url in str(response.content))

    def test_Single_Photo_view(self):
        """Test image on single photo view."""
        image1 = Photo.objects.all()[0]
        image2 = Photo.objects.all()[1]
        user1 = User.objects.first()
        image1.owner = user1.profile
        image2.owner = user1.profile
        image1.save()
        image2.save()
        self.client.force_login(user1)
        response = self.client.get(reverse_lazy("singlephoto", kwargs={'photoid': image1.id}))
        self.assertTrue(image1.image_file.url in str(response.content))

    def test_logged_in_user_sees_their_albums_on_albums(self):
        """Logged in user should see their albums."""
        user = UserFactory.create()
        album1 = Album.objects.first()
        album2 = Album.objects.all()[1]
        user.profile.album.add(album1)
        user.profile.album.add(album2)
        user.save()
        self.client.force_login(user)
        response = self.client.get(reverse_lazy("singlealbum", kwargs={'albumid': album1.id}))
        self.assertTrue(album1.description in str(response.content))

    def test_logged_in_user_does_not_see_other_albums(self):
        """Logged in user should see their albums."""
        user1 = UserFactory.create()
        user2 = UserFactory.create()
        album1 = Album.objects.first()
        album2 = Album.objects.all()[1]
        user1.profile.album.add(album1)
        user1.profile.album.add(album2)
        user1.save()
        user2.save()
        self.client.force_login(user2)
# <<<<<<< HEAD
        # response = self.client.get(reverse_lazy("singlealbum", kwargs={'albumid': album1.id}))
        # self.assertTrue(response.status_code == 301)
# =======
        response = self.client.get('/images/albums/' + str(album1.id), {"follow": True}, follow=True)
        self.assertTrue(response.status_code == 404)

    def test_single_photo_view_returns_404(self):
        """Test image on single photo view."""
        image1 = Photo.objects.all()[0]
        image2 = Photo.objects.all()[1]
        user1 = User.objects.first()
        user2 = UserFactory.create()
        image1.owner = user1.profile
        image2.owner = user1.profile
        image1.save()
        image2.save()
        user2.save()
        self.client.force_login(user2)

        response = self.client.get(reverse_lazy("singlephoto", kwargs={'photoid': image1.id}))
        self.assertTrue(response.status_code == 404)
