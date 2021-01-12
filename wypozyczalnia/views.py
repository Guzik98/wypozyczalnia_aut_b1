from django.shortcuts import render, redirect
from .models import Gallery, Car, AditionalEquipment, Model, Engine, FuelType
from .forms import CarForm, GalleryForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages



def home(request):
    gallerys = Gallery.objects.all()
    return render(request, 'wypozyczalnia/home.html', { 'gallerys':gallerys })

def addcar(request):
    #form = CarForm()
    #return render(request, 'wypozyczalnia/newCar.html', { 'form' :form })
    if request.method == 'POST':  
        form = CarForm(request.POST)
        form2 = GalleryForm(request.POST)
        form.save()
        form2.save()
        return redirect('wypozyczalnia-home')
    else:
        form = CarForm()
        form2 = GalleryForm()
    return render(request, 'wypozyczalnia/newcar.html',{'form':form},{'form2':form2})
    
