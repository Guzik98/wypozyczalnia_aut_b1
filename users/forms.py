from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from phonenumber_field.formfields import PhoneNumberField
from .models import Account
#from bootstrap_datepicker_plus import DateTimePickerInput
from django.contrib.admin.widgets import AdminDateWidget
import datetime
from django.core.exceptions import ValidationError

class DateInput(forms.DateInput):
    input_type = 'date'


def Nr_dokumentu_validacja(value):
     if len(value)<9:
       raise ValidationError('Nieprawidlowy numer dokumentu')



def not_past_days(value):
    value = value.strftime('%y-%m-%d')
    today = datetime.date.today().strftime('%y-%m-%d')
    if value<today:
        raise ValidationError('Przeterminowane prawo jazdy')

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    Data_waznosc_prawo_jazdy = forms.DateField(widget=DateInput(), validators=[not_past_days], label = 'Data ważności prawa jazdy' ) 
    Nr_dokumentu = forms.CharField(validators=[Nr_dokumentu_validacja], label = 'Numer dokumentu prawa jazdy')
    phone = PhoneNumberField( label = 'Numer telefonu z numerem kierunkowym')
    class Meta:
        model = Account
        wigdets = {
            'Data_waznosc_prawo_jazdy' : DateInput(
            attrs={'class': 'picker',  'autocomplete': 'off'}),
        }
        labels = {
            "username": "Nazwa użytkownika",
            "first_name": "Imię",
            "last_name": "Nazwisko",
            "phone": "Numer telefonu",
            "Data_waznosc_prawo_jazdy": "Prawo jazdy ważne do",
            "Nr_dokumentu": "Numer indetyfikujący prawo jazdy",
        }
        fields = ['email', 'username','first_name','last_name','phone',  'Data_waznosc_prawo_jazdy','Nr_dokumentu', 'password1', 'password2',]

class EmployeeRegisterForm(UserCreationForm):
    email = forms.EmailField()
    Data_waznosc_prawo_jazdy = forms.DateField(widget=DateInput(), validators=[not_past_days], label = 'Data ważności prawa jazdy' ) 
    Nr_dokumentu = forms.CharField(validators=[Nr_dokumentu_validacja], label = 'Numer dokumentu prawa jazdy')
    phone = PhoneNumberField( label = 'Numer telefonu z numerem kierunkowym')
    class Meta:
        model = Account
        labels = {
            "first_name": "Imię",
            "last_name": "Nazwisko",
            "username": "Nazwa użytkownika",
            "phone": "Numer telefonu",
            "Data_waznosc_prawo_jazdy": "Prawo jazdy ważne do",
            "Nr_dokumentu": "Numer indetyfikujący prawo jazdy",
            "is_staff": "Pracownik",
            }
        
        fields = [ 'email','first_name','last_name', 'username','phone','is_staff','Data_waznosc_prawo_jazdy','Nr_dokumentu', 'password1', 'password2',]

class ManagerRegisterForm(UserCreationForm):
    email = forms.EmailField()
    Data_waznosc_prawo_jazdy = forms.DateField(widget=DateInput(), validators=[not_past_days], label = 'Data ważności prawa jazdy' ) 
    Nr_dokumentu = forms.CharField(validators=[Nr_dokumentu_validacja], label = 'Numer dokumentu prawa jazdy')
    phone = PhoneNumberField( label = 'Numer telefonu z numerem kierunkowym')
    class Meta:
        labels = {
            "first_name": "Imię",
            "last_name": "Nazwisko",
            "username": "Nazwa użytkownika",
            "phone": "Numer telefonu",
            "Data_waznosc_prawo_jazdy": "Prawo jazdy ważne do",
            "Nr_dokumentu": "Numer indetyfikujący prawo jazdy",
            "is_staff": "Pracownik",
                }
        
        model = Account
        fields = [ 'email', 'first_name','last_name', 'username','phone','is_staff','Data_waznosc_prawo_jazdy','Nr_dokumentu','password1', 'password2',]

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    Data_waznosc_prawo_jazdy = forms.DateField(widget=DateInput(), validators=[not_past_days], label = 'Data ważności prawa jazdy' ) 
    Nr_dokumentu = forms.CharField(validators=[Nr_dokumentu_validacja], label = 'Numer dokumentu prawa jazdy')
    phone = PhoneNumberField(label='Numer telefonu z numerem kierunkowym')
    class Meta:
        model = Account
        labels = {
            "username": "Nazwa użytkownika",
            "first_name": "Imię",
            "last_name": "Nazwisko",
            "phone": "Numer telefonu",
            "Data_waznosc_prawo_jazdy": "Prawo jazdy ważne do",
            "Nr_dokumentu": "Numer indetyfikujący prawo jazdy",
        }
        fields = ['email', 'first_name', 'last_name',
                  'phone', 'Data_waznosc_prawo_jazdy', 'Nr_dokumentu', ]
