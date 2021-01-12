from django.contrib import admin
from users.models import Account
from . import models
admin.site.register(Account)

class RegisterAdmin(admin.ModelAdmin):
    list_display = ('self', 'email', 'username', 'password', 'first_name', 'last_name', 'phone', 'is_staff')