from django import forms
from .models import Rezerwacja
import datetime
from django.core.exceptions import ValidationError

class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'

def not_past_days(value):
    value = value.strftime('%y-%m-%d')
    today = datetime.date.today().strftime('%y-%m-%d')
    if value<today:
        raise ValidationError('Nie możesz dokonać odbioru lub zwrotu wcześniej niż teraz')



class RezerwacjaForm(forms.ModelForm):
    data_odbioru = forms.DateField(widget=DateInput(), validators=[not_past_days])
    data_zwrotu = forms.DateField(widget=DateInput(), validators=[not_past_days])
    godzina_odbioru = forms.TimeField(widget=TimeInput())
    godzina_zwrotu =  forms.TimeField(widget=TimeInput())

    class Meta:
        model = Rezerwacja
        fields = ('miejsce_odbioru','data_odbioru','godzina_odbioru','miejsce_zwrotu','data_zwrotu','godzina_zwrotu')
