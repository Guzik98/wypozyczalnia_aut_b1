from django import forms

from .models import Post
from django.core.exceptions import ValidationError

def walidacjaTextu(value):
     if len(value)<10:
       raise ValidationError('Upewnij się, że treść zawiera od 10 do 150 znaków.')
class PostForm(forms.ModelForm):
    text=forms.CharField(validators=[walidacjaTextu], label = 'Treść', widget=forms.Textarea)
    class Meta:
        model = Post
        labels = {
            'title': 'Tytuł',
            'zdjecie': 'Zdjęcie',
        }
        fields = ('title', 'text','zdjecie')