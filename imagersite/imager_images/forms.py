from django import forms
from .models import Photo

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['title', 'description', 'image']
        title = forms.CharField(label='title', max_length=50)
        description = forms.CharField(label='description', max_length=200)
