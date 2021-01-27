from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils.translation import ugettext_lazy as _
from phonenumber_field.formfields import PhoneNumberField

class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, first_name, last_name, phone,Data_waznosc_prawo_jazdy,Nr_dokumentu,password=None):
        if not email:
            raise ValueError("Użytkownik musi podać adres e-mail")
        if not username:
            raise ValueError("Users must have an username")
        if not first_name:
            raise ValueError("Użytkownik musi podać imię")
        if not last_name:
            raise ValueError("Użytkownik musi podać nazwisko")
        if not phone:
            raise ValueError("Użytkownik musi podać numer telefonu")
        if not Data_waznosc_prawo_jazdy:
            raise ValueError("Użytkownik musi podać date waznosc prawa  jazdy")
        if not Nr_dokumentu:
            raise ValueError("Użytkownik musi podać numer prawa jazdy")

        user  = self.model(
                email=self.normalize_email(email),
                username=username,
                first_name=first_name,
                last_name=last_name,
                phone=phone,
                Data_waznosc_prawo_jazdy = Data_waznosc_prawo_jazdy,
                Nr_dokumentu = Nr_dokumentu,
            )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password, first_name, last_name, phone, Nr_dokumentu,Data_waznosc_prawo_jazdy):
        user  = self.create_user(
                email=self.normalize_email(email),
                password=password,
                username=username,
                first_name=first_name,
                last_name=last_name,
                phone=phone,
                Data_waznosc_prawo_jazdy = Data_waznosc_prawo_jazdy,
                Nr_dokumentu = Nr_dokumentu,

            )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.is_manager = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    email 					= models.EmailField(verbose_name="email", max_length=60, unique=True)
    username 				= models.CharField(max_length=30, unique=True)
    date_joined				= models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login				= models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin				= models.BooleanField(default=False)
    is_active				= models.BooleanField(default=True)
    is_staff				= models.BooleanField(default=False)
    is_superuser			= models.BooleanField(default=False)
    is_manager              = models.BooleanField(default=False)
    first_name 				= models.CharField(max_length=30)
    last_name               = models.CharField(max_length=30)
    phone                   = models.CharField(max_length=12)
    Data_waznosc_prawo_jazdy        = models.CharField(max_length=10)
    Nr_dokumentu             = models.CharField(max_length=9)
    


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','first_name','last_name','phone','Data_waznosc_prawo_jazdy','Nr_dokumentu']

    objects = MyAccountManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
