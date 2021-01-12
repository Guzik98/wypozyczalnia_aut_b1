from django import forms
from .models import Car, Gallery

class CarForm(forms.ModelForm):

    class Meta:
        model = Car       
        fields = ('nazwa','rok_produkcji','cena_za_godzine','dostepnosc','klimatyzacja','ilosc_drzwi','model','silnik','opcjonalne_wyposazenie',)

class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery       
        fields = ('photo',)