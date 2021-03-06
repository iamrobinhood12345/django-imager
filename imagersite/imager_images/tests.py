from django.conf import settings
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.utils import timezone
from django.urls import reverse_lazy
from imager_profile.models import ImagerProfile
from imager_images.models import Photo, Album
import factory





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
    title = factory.Sequence(lambda n: "Photo {}".format(n))
    image_file = SimpleUploadedFile(name='image_1.jpg', content=open('imagersite/static/images/image_1.jpg', 'rb').read(), content_type='image/jpeg')


class AlbumFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Album
    title = factory.Sequence(lambda n: "Album {}".format(n))
    cover_image = SimpleUploadedFile(name='image_1.jpg', content=open('imagersite/static/images/image_1.jpg', 'rb').read(), content_type='image/jpeg')
    description = "Some Album"


class ImageTestCase(TestCase):
    """Image Test Class."""

    def setUp(self):
        """User, photos, and album setup for tests."""
        self.users = [UserFactory.create() for i in range(10)]
        self.photo = [ImageFactory.create() for i in range(10)]
        self.album = [AlbumFactory.create() for i in range(10)]

    def test_photo_title(self):
        """Test that photo has a title."""
        self.assertTrue("Photo" in Photo.objects.first().title)

    def test_photo_has_description(self):
        """Test that the photo description field can be assigned."""
        photo = Photo.objects.first()
        photo.description = "Works."
        photo.save()
        self.assertTrue(Photo.objects.first().description == "Works.")

    def test_photo_is_published(self):
        """photo should have a published field."""
        photo = Photo.objects.first()
        photo.published = 'public'
        photo.save()
        self.assertTrue(Photo.objects.first().published == "public")

    def test_photo_date_modified(self):
        """photo should have a date modified default."""
        photo = Photo.objects.first()
        self.assertTrue(photo.date_modified)

    def test_photo_date_uploaded(self):
        """photo should have a default date uploaded."""
        photo = Photo.objects.first()
        self.assertTrue(photo.date_uploaded)

    def test_photo_no_date_date_published(self):
        """Test that the photo does not have a date published before assignment."""
        photo = Photo.objects.first()
        self.assertFalse(photo.date_published)

    def test_photo_date_date_published(self):
        """Test that the photo has a date published after assignment."""
        photo = Photo.objects.first()
        photo.date_published = timezone.now
        self.assertTrue(photo.date_published)

    def test_photo_has_no_owner(self):
        """Test that photo has no owner."""
        photo = Photo.objects.first()
        self.assertFalse(photo.owner)

    def test_photo_has_owner(self):
        """Photo should have owner after assignment."""
        photo = Photo.objects.first()
        user1 = User.objects.first()
        photo.owner = user1.profile
        self.assertTrue(photo.owner)

    def test_owner_has_photo(self):
        """Owner should be associated with the photo."""
        photo = Photo.objects.first()
        user1 = User.objects.first()
        photo.owner = user1.profile
        photo.save()
        self.assertTrue(user1.profile.photo.count() == 1)

    def test_two_photos_have_owner(self):
        """Two pics should have same owner."""
        photo1 = Photo.objects.all()[0]
        photo2 = Photo.objects.all()[1]
        user1 = User.objects.first()
        photo1.owner = user1.profile
        photo2.owner = user1.profile
        photo1.save()
        photo2.save()
        self.assertTrue(photo1.owner == user1.profile)
        self.assertTrue(photo2.owner == user1.profile)

    def test_owner_has_two_photos(self):
        """Test that owner has two photo."""
        photo1 = Photo.objects.all()[0]
        photo2 = Photo.objects.all()[1]
        user1 = User.objects.first()
        photo1.owner = user1.profile
        photo2.owner = user1.profile
        photo1.save()
        photo2.save()
        self.assertTrue(user1.profile.photo.count() == 2)

    def test_photo_has_no_album(self):
        """Test that the photo is in an album."""
        photo = Photo.objects.first()
        self.assertTrue(photo.albums_of_photos.count() == 0)

    def test_photo_has_album(self):
        """Test that the photo is in an album."""
        photo = Photo.objects.first()
        album1 = Album.objects.first()
        photo.albums_of_photos.add(album1)
        self.assertTrue(photo.albums_of_photos.count() == 1)

    def test_album_has_no_photo(self):
        """Test that an album has no photo before assignemnt."""
        album1 = Album.objects.first()
        self.assertTrue(album1.images.count() == 0)

    def test_album_has_photo(self):
        """Test that an album has an photo after assignemnt."""
        photo = Photo.objects.first()
        album1 = Album.objects.first()
        photo.albums_of_photos.add(album1)
        self.assertTrue(photo.albums_of_photos.count() == 1)

    def test_two_photos_have_album(self):
        """Test that two photos have same album."""
        photo1 = Photo.objects.all()[0]
        photo2 = Photo.objects.all()[1]
        album1 = Album.objects.first()
        photo1.albums_of_photos.add(album1)
        photo2.albums_of_photos.add(album1)
        photo1.save()
        photo2.save()
        self.assertTrue(photo1.albums_of_photos.all()[0] == album1)
        self.assertTrue(photo2.albums_of_photos.all()[0] == album1)

    def test_album_has_two_photos(self):
        photo1 = Photo.objects.all()[0]
        photo2 = Photo.objects.all()[1]
        album1 = Album.objects.first()
        photo1.albums_of_photos.add(album1)
        photo2.albums_of_photos.add(album1)
        photo1.save()
        photo2.save()
        self.assertTrue(album1.images.count() == 2)

    def test_photo_has_two_albums(self):
        """Test that an photo has two albums."""
        photo1 = Photo.objects.first()
        album1 = Album.objects.all()[0]
        album2 = Album.objects.all()[1]
        photo1.albums_of_photos.add(album1)
        photo1.albums_of_photos.add(album2)
        photo1.save()
        self.assertTrue(photo1.albums_of_photos.count() == 2)

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
        """Album should have an owner after assignment."""
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
        """Two albums should have same owner."""
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
        """Owner should have two albums."""
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
        """Test photos on photo view."""
        photo1 = Photo.objects.all()[0]
        photo2 = Photo.objects.all()[1]
        user1 = User.objects.first()
        photo1.owner = user1.profile
        photo2.owner = user1.profile
        photo1.save()
        photo2.save()
        self.client.force_login(user1)
        response = self.client.get(reverse_lazy("allphotos"))
        self.assertTrue(photo1.image_file.url in str(response.content))

    def test_Single_Photo_view(self):
        """Test photo on single photo view."""
        photo1 = Photo.objects.all()[0]
        photo2 = Photo.objects.all()[1]
        user1 = User.objects.first()
        photo1.owner = user1.profile
        photo2.owner = user1.profile
        photo1.save()
        photo2.save()
        self.client.force_login(user1)
        response = self.client.get(reverse_lazy("singlephoto", kwargs={'photoid': photo1.id}))
        self.assertTrue(photo1.image_file.url in str(response.content))

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
        response = self.client.get('/images/albums/' + str(album1.id), {"follow": True}, follow=True)
        self.assertTrue(response.status_code == 403)

    def test_single_photo_view_returns_404(self):
        """Test photo on single photo view."""
        photo1 = Photo.objects.all()[0]
        photo2 = Photo.objects.all()[1]
        user1 = User.objects.first()
        user2 = UserFactory.create()
        photo1.owner = user1.profile
        photo2.owner = user1.profile
        photo1.save()
        photo2.save()
        user2.save()
        self.client.force_login(user2)
        response = self.client.get(reverse_lazy("singlephoto", kwargs={'photoid': photo1.id}))
        self.assertTrue(response.status_code == 403)
