from django import forms
from .models import Car

class CarForm(forms.ModelForm):

    class Meta:
        model = Car       
        fields = ('nazwa',
        'rok_produkcji',
        'cena_za_godzine',
        'dostepnosc',
        'klimatyzacja',
        'ilosc_drzwi',
        'model',
        'silnik',
        'opcjonalne_wyposazenie',
        'photo',)
