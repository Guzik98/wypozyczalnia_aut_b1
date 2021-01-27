from django.shortcuts import render, redirect
from .models import Rezerwacja
from wypozyczalnia.models import Car
from .forms import RezerwacjaForm
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

@login_required
def add_rezerwacja(request,pk):
    car = get_object_or_404(Car, pk=pk)
    if request.method == 'POST':
        form = RezerwacjaForm(request.POST)
        if form.is_valid():
            rezerwacja = form.save(commit=False)
            rezerwacja.osoba_wypozyczajaca = request.user
            rezerwacja.auto_wypozyczane = car
            car.dostepnosc = False
            car.save()
            form.save()
            return redirect('wypozyczalnia-home')
        else:
            print(form.errors)
    else:
        form = RezerwacjaForm()
    return render(request, 'rezerwacja/rezerwacja.html',{'form':form})
