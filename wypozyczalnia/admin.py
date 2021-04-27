from django.contrib import admin
from . import models

@admin.register(models.Model)
class ModelAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(models.FuelType)
class FuelTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(models.Engine)
class EngineAdmin(admin.ModelAdmin):
    list_display = ('name', 'power', 'consumation', 'fuel_type') 
    search_fields = ('name',)
    list_filter = ('name', 'consumation')

@admin.register(models.AditionalEquipment)
class ModelAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(models.Segment)
class ModelAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(models.Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('nazwa', 'model', 'rok_produkcji', 'silnik', 'cena_za_godzine', 'dostepnosc','klimatyzacja','ilosc_drzwi','segment')
    search_fields = ('nazwa',)
    list_editable = ('cena_za_godzine', 'dostepnosc')
    list_filter = ('dostepnosc',)
    list_select_related = ('model', 'silnik')


    def model(self, obj):
        return obj.model

    def engine(self, obj):
        return obj.engine


@admin.register(models.Rating)
class RateAdmin(admin.ModelAdmin):
    list_display = ('user', 'car', 'date', 'rate','text') 
    search_fields = ('user',)