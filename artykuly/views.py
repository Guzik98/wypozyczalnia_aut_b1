from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, user_passes_test
# Create your views here.

def displayArticle(request):
    articles = Post.objects.all()
    return render(request, 'artykuly/wyswietlanieArtykulu.html', { 'articles':articles })

@user_passes_test(lambda u: u.is_staff)
def addArticle(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            dodanyArtykul = form.save(commit=False)
            dodanyArtykul.author = request.user
            form.save()
            return redirect('artykuly_widok')
        else:
            print(form.errors)
    else:
        form = PostForm()
    return render(request, 'artykuly/dodanieArtykulu.html',{'form':form})
