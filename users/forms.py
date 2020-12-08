from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from phonenumber_field.formfields import PhoneNumberField


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    phone = PhoneNumberField()

    class Meta:
        model = User
        fields = ['username','first_name','last_name','phone', 'email', 'password1', 'password2',]
