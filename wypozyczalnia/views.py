from django.shortcuts import render, redirect
from .models import Car, AditionalEquipment, Model, Engine, FuelType, Rating
from .forms import CarForm, SegmentForm, RateForm
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
    rate = Rating.objects.order_by('-date')
    return render(request, 'wypozyczalnia/car_detail.html', {'car': car, 'rate': rate})


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


@user_passes_test(lambda u: u.is_staff)
def addsegment(request):
    if request.method == 'POST':
        form = SegmentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('wypozyczalnia-home')
        else:
            print(form.errors)
    else:
        form = SegmentForm()
    return render(request, 'wypozyczalnia/addSegment.html',{'form':form})

@login_required
def Rate(request, pk):
    car = get_object_or_404(Car, pk=pk)
    user = request.user
    if request.method == 'POST':
        form = RateForm(request.POST)
        if form.is_valid():
            rate = form.save(commit=False)
            rate.user = user
            rate.car = car
            rate.save()
            return redirect('car_detail', pk)
        else:
            print(form.errors)
    else:
        form = RateForm()
    return render(request, 'wypozyczalnia/car_rating.html',{'form':form})

