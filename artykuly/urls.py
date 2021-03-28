from django.urls import path
from . import views


urlpatterns = [
    path('', views.displayArticle, name='artykuly_widok'),
    path('newArticle/', views.addArticle, name="addArticle"),
    path('article/<int:pk>/', views.article_detail, name='article_detail'),
    path('article/<int:pk>/edit', views.article_edit, name='article_edit'),
    path('article/<int:pk>/delete', views.article_delete, name='article_delete'),
    ]
