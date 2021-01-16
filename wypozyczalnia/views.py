from django.shortcuts import render, redirect
from .models import Car, AditionalEquipment, Model, Engine, FuelType
from .forms import CarForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages



def home(request):
    cars = Car.objects.all()
    return render(request, 'wypozyczalnia/home.html', { 'cars':cars })

def addcar(request):
    if request.method == 'POST':  
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('wypozyczalnia-home')
        else:
            print(form.errors)
    else:
        form = CarForm()
    return render(request, 'wypozyczalnia/newCar.html',{'form':form})
    
