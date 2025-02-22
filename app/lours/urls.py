from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('auth/', auth_views.LoginView.as_view(), name='auth'),
    path('notes/', views.notes, name='notes'),
    path('posts/', views.posts, name='posts'),
]
