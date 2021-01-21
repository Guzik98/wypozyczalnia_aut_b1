from django import forms
from .models import Rezerwacja

class RezerwacjaForm(forms.ModelForm):

    class Meta:
        model = Rezerwacja
        fields = ('miejsce_odbioru','data_odbioru','godzina_odbioru','miejsce_zwrotu','data_zwrotu','godzina_zwrotu')
