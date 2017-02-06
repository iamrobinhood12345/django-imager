from django import forms
from .models import Photo, Album


class PhotoForm(forms.ModelForm):
    """Form to add photo."""

    class Meta:
        """Define what is to be put in the model."""

        model = Photo
        fields = ['title', 'description', 'image_file', 'tags', 'published']
        title = forms.CharField(label='title', max_length=50)
        description = forms.CharField(label='description', max_length=200)


class AlbumForm(forms.ModelForm):
    """Form to add album."""

    class Meta:
        """Define what is to be put in the model."""

        model = Album
        fields = ['title', 'description', 'cover_image', 'tags', 'published']
        title = forms.CharField(label='title', max_length=50)
        description = forms.CharField(label='description', max_length=200)


class EditAlbumForm(forms.ModelForm):
    """Form to edit album."""

    class Meta:
        """Define what should be in the form and exclude fields."""

        model = Album
        exclude = [
            'owner',
            'date_uploaded',
            'date_modified',
            'date_published',
            'owner'
        ]
        fields = ['title', 'description', 'cover_image', 'tags', 'published']
        title = forms.CharField(label='title', max_length=50)
        description = forms.CharField(label='description', max_length=200)


class EditPhotoForm(forms.ModelForm):
    """Form to edit photos."""

    class Meta:
        """Define what should be in the form."""

        model = Photo
        exclude = [
            'owner',
            'date_uploaded',
            'date_modified',
            'date_published',
            'photo'
        ]
        fields = ['title', 'description', 'image_file', 'tags', 'published']
        title = forms.CharField(label='title', max_length=50)
        description = forms.CharField(label='description', max_length=200)
