from django import forms
from .models import Rezerwacja

import datetime
from django.core.exceptions import ValidationError

class DateInput(forms.DateInput):
    input_type = 'date'
class TimeInput(forms.TimeInput):
    input_type = 'time'
class RezerwacjaForm(forms.ModelForm):
    data_odbioru = forms.DateField(widget=DateInput())
    data_zwrotu = forms.DateField(widget=DateInput())
    godzina_odbioru = forms.TimeField(widget=TimeInput())
    godzina_zwrotu = forms.TimeField(widget=TimeInput())
    class Meta:
        model = Rezerwacja
        fields = ('miejsce_odbioru', 'data_odbioru', 'godzina_odbioru',
                  'miejsce_zwrotu', 'data_zwrotu', 'godzina_zwrotu')
    def clean(self):
        today = datetime.date.today().strftime('%y-%m-%d')
        cleaned_data = super().clean()
        godzina_odbioru = cleaned_data.get("godzina_odbioru").strftime('%H:%M')
        godzina_zwrotu = cleaned_data.get("godzina_zwrotu").strftime('%H:%M')
        data_odbioru = cleaned_data.get("data_odbioru").strftime('%y-%m-%d')
        data_zwrotu = cleaned_data.get("data_zwrotu").strftime('%y-%m-%d')
        if data_odbioru > data_zwrotu: 
            raise ValidationError("Data zwrotu nie może być wcześniejsza niż data odbioru")
        if data_odbioru < today or data_zwrotu < today:
            raise ValidationError('Nie możesz dokonać odbioru lub zwrotu wcześniej niż teraz')
        if data_odbioru == data_zwrotu and godzina_odbioru >= godzina_zwrotu :
            raise ValidationError('Nie możesz dokonać rezerwacji jeśli godzina zwrotu jest wcześniejsza lub równa niz godzina odbioru')
