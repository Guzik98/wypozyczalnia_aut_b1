from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='wypozyczalnia-home'),
    path('newCar/', views.addcar, name="newCar"),
]