from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from phonenumber_field.formfields import PhoneNumberField
from .models import Account
from bootstrap_datepicker_plus import DateTimePickerInput
from django.contrib.admin.widgets import AdminDateWidget
import datetime
from django.core.exceptions import ValidationError

class DateInput(forms.DateInput):
    input_type = 'date'

def not_past_days(value):
    value = value.strftime('%y-%m-%d')
    today = datetime.date.today().strftime('%y-%m-%d')
    if value<today:
        raise ValidationError('Przeterminowane prawo jazdy')

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    driving_license = forms.DateField(widget=DateInput(), validators=[not_past_days])
    class Meta:
        model = Account
        wigdets = {
            'driving_license' : DateInput(
            attrs={'class': 'picker',  'autocomplete': 'off'}),
        }
        labels = {
            "username": "Nazwa użytkownika",
            "first_name": "Imię",
            "last_name": "Nazwisko",
            "phone": "Numer telefonu",
            "driving_license": "Prawo jazdy ważne do",
        }

        phone = PhoneNumberField()
        fields = ['email', 'username','first_name','last_name','phone',  'driving_license', 'password1', 'password2',]

class EmployeeRegisterForm(UserCreationForm):
    email = forms.EmailField()
    driving_license = forms.DateField(widget=DateInput(), validators=[not_past_days])
    class Meta:
        model = Account
        labels = {
            "first_name": "Imię",
            "last_name": "Nazwisko",
            "username": "Nazwa użytkownika",
            "phone": "Numer telefonu",
            "driving_license": "Prawo jazdy ważne do",
            "is_staff": "Pracownik",
            }
        phone = PhoneNumberField()
        fields = [ 'email','first_name','last_name', 'username','phone','is_staff','driving_license', 'password1', 'password2',]

class ManagerRegisterForm(UserCreationForm):
    email = forms.EmailField()
    driving_license = forms.DateField(widget=DateInput(), validators=[not_past_days])
    class Meta:
        labels = {
            "first_name": "Imię",
            "last_name": "Nazwisko",
            "username": "Nazwa użytkownika",
            "phone": "Numer telefonu",
            "driving_license": "Prawo jazdy ważne do",
            "is_staff": "Pracownik",
                }
        phone = PhoneNumberField()
        model = Account
        fields = [ 'email', 'first_name','last_name', 'username','phone','is_staff','driving_license','password1', 'password2',]

class UserUpdateForm(UserChangeForm):
    email = forms.EmailField()
    driving_license = forms.DateField(widget=DateInput(), validators=[not_past_days])
    class Meta:
        model = Account
        labels = {
            "username": "Nazwa użytkownika",
            "first_name": "Imię",
            "last_name": "Nazwisko",
            "phone": "Numer telefonu",
            "driving_license": "Prawo jazdy ważne do",
        }
        phone = PhoneNumberField()
        fields = [ 'email','first_name','last_name','phone', 'driving_license', 'password',]
