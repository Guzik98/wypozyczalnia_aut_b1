from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='wypozyczalnia-home'),
    path('newCar/', views.addcar, name="newCar"),
    path('addSegment/', views.addsegment, name="addSegment"),
    path('car/<int:pk>/', views.car_detail, name='car_detail'),
    path('car/<int:pk>/edit', views.car_edit, name='car_edit'),
    path('car/<int:pk>/delete', views.car_delete, name='car_delete'),
    path('car/<int:pk>/rate', views.Rate, name='car_rate'),
    ]
