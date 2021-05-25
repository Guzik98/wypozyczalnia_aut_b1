from django.shortcuts import render, redirect
from .models import Rezerwacja
from wypozyczalnia.models import Car
from .forms import RezerwacjaForm
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required,user_passes_test
from django.utils import timezone

@user_passes_test(lambda u: u.is_staff)
def search(request):
    data_odbioru_html_date = request.GET.get('data_odbioru_html')
    data_zwrotu_html_date = request.GET.get('data_zwrotu_html')
    rezerwacje = Rezerwacja.objects.all()
    if data_odbioru_html_date != '' and data_odbioru_html_date is not None:
        rezerwacje = rezerwacje.filter(data_odbioru__lte=data_odbioru_html_date)
        rezerwacje = rezerwacje.filter(data_odbioru__gte=data_odbioru_html_date)
    if data_zwrotu_html_date != '' and data_zwrotu_html_date is not None:
        rezerwacje = rezerwacje.filter(data_zwrotu__lte=data_zwrotu_html_date)
        rezerwacje = rezerwacje.filter(data_zwrotu__gte=data_zwrotu_html_date)
    return render(request, 'rezerwacja/rezerwacja_wyswietlanie.html', {'rezerwacje':rezerwacje, 'data_odbioru_html_date':data_odbioru_html_date, 'data_zwrotu_html_date':data_zwrotu_html_date})




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


