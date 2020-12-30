from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from phonenumber_field.formfields import PhoneNumberField
from .models import Account

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    phone = PhoneNumberField()
    driving_license = forms.DateField()
    class Meta:
        model = Account
        fields = ['first_name','last_name','phone', 'email','driving_license', 'password1', 'password2',]


class EmployeeRegisterForm(UserCreationForm):
    email = forms.EmailField()
    phone = PhoneNumberField()
    class Meta:
        model = Account
        fields = ['first_name','last_name', 'username','phone', 'email','is_staff', 'password1', 'password2',]

class ManagerRegisterForm(UserCreationForm):
    email = forms.EmailField()
    phone = PhoneNumberField()
    class Meta:
        model = Account
        fields = ['first_name','last_name', 'username','phone', 'email','is_staff','password1', 'password2',]

class UserUpdateForm(UserChangeForm):
    email = forms.EmailField()
    phone = PhoneNumberField()
    driving_license = forms.DateField()
    class Meta:
        model = Account
        fields = ['first_name','last_name','phone', 'email','driving_license', 'password',]
