from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm, EmployeeRegisterForm, UserUpdateForm
from django.contrib.auth.decorators import login_required, user_passes_test


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Twoje konto zostało utworzone! Możesz się teraz zalogować')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html',{'form':form})

@user_passes_test(lambda u: u.is_manager)
def registerEmployee(request):
    if request.method == 'POST':
        form = EmployeeRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Twoje konto zostało utworzone! Możesz się teraz zalogować')
            return redirect('login')
    else:
        form = EmployeeRegisterForm()
    return render(request, 'users/register.html',{'form':form})

@login_required
def edit_account_redirect(request):
    if request.method == 'POST':
        edit_form = UserUpdateForm(request.POST,instance=request.user)
        if edit_form.is_valid() :
            edit_form.save()
            messages.success(request,'Zmieniłeś dane konta!')
            return redirect('wypozyczalnia-home')
    else:
        edit_form = UserUpdateForm(instance=request.user)

    context={'edit_form': edit_form}
    return render(request, 'users/edit_account.html',context )
