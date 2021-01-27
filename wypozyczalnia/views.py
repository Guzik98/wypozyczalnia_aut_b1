from django.shortcuts import render, redirect
from .models import Car, AditionalEquipment, Model, Engine, FuelType
from .forms import CarForm
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, user_passes_test



def home(request):
    cars = Car.objects.all()
    return render(request, 'wypozyczalnia/home.html', { 'cars':cars })

@user_passes_test(lambda u: u.is_staff)
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

def car_detail(request, pk):
    car = get_object_or_404(Car, pk=pk)
    return render(request, 'wypozyczalnia/car_detail.html', {'car': car})

@user_passes_test(lambda u: u.is_staff)
def car_edit(request, pk):
    car = get_object_or_404(Car, pk=pk)
    if request.method == "POST":
        form = CarForm(request.POST, request.FILES, instance=car)
        if form.is_valid():
            car = form.save(commit=False)
            car.save()
            return redirect('wypozyczalnia-home')
    else:
        form = CarForm(instance=car)
    return render(request, 'wypozyczalnia/car_edit.html', {'form': form})

@user_passes_test(lambda u: u.is_staff)
def car_delete(request, pk):
    car = get_object_or_404(Car, pk=pk)
    if request.method == "POST":
        form = CarForm(request.POST, instance=car)
        if form.is_valid():
            car = form.save(commit=False)
            car.delete()
            return redirect('wypozyczalnia-home')
    else:
        form = CarForm(instance=car)
    return render(request, 'wypozyczalnia/car_delete.html', {'form': form})
