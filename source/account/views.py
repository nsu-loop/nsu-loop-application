from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from account.models import User
from django.contrib.auth import authenticate, login
from django.contrib.admin import forms


# Create your views here.


def home(request):
    return render(request, 'account/signup.html')


def user_login(request):
 
    
    return render(request, 'account/login.html')




def signup(request):
   
       
    return render(request, 'account/signup.html')







