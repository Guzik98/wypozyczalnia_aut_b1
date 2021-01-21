from django.contrib import admin
from . import models

@admin.register(models.Miejsce)
class ModelAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(models.Rezerwacja)
class CarAdmin(admin.ModelAdmin):
    list_display = ('miejsce_odbioru', 'data_odbioru', 'godzina_odbioru', 'miejsce_zwrotu', 'data_zwrotu', 'godzina_zwrotu',)

