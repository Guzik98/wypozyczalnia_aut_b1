from django.shortcuts import render, redirect, get_object_or_404
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

def article_detail(request, pk):
    article = get_object_or_404(Post, pk=pk)
    return render(request, 'artykuly/article_detail.html', {'article': article})


@user_passes_test(lambda u: u.is_staff)
def article_edit(request, pk):
    article = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            article = form.save(commit=False)
            article.save()
            return redirect('artykuly_widok')
    else:
        form = PostForm(instance=article)
    return render(request, 'artykuly/article_edit.html', {'form': form})

@user_passes_test(lambda u: u.is_staff)
def article_delete(request, pk):
    article = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save(commit=False)
            article.delete()
            return redirect('artykuly_widok')
    else:
        form = PostForm(instance=article)
    return render(request, 'artykuly/article_delete.html', {'form': form})
