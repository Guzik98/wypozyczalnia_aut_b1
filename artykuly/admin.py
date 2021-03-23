from django.contrib import admin
from . import models

@admin.register(models.Post)
class CarAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'zdjecie', 'text', 'published_date',)
