from django import forms
from .models import Car
from django.utils.translation import ugettext_lazy as _

class CarForm(forms.ModelForm):

    class Meta:
        model = Car
        fields = (_('nazwa'),
        _('rok_produkcji'),
        _('cena_za_godzine'),
        _('dostepnosc'),
        _('klimatyzacja'),
        _('ilosc_drzwi'),
        _('model'),
        _('silnik'),
        _('opcjonalne_wyposazenie'),
        _('zdjecie'),)
