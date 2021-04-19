from django.contrib import admin
from django.urls import path
from account import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup', views.signup, name='signup'),
    path('login', views.user_login, name='login'),
   
]
