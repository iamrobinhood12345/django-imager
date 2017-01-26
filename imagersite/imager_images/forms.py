from django import forms
from .models import Photo, Album

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['title', 'description', 'image_file']
        title = forms.CharField(label='title', max_length=50)
        description = forms.CharField(label='description', max_length=200)


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['title', 'description', 'cover_image']
        title = forms.CharField(label='title', max_length=50)
        description = forms.CharField(label='description', max_length=200)
