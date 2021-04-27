from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from account.models import User
from django.contrib.auth import authenticate, login
from django.contrib.admin import forms




# Create your views here.

def home(request):
    return render(request, 'account/signup.html')

def signup(request):
    if request.method=='POST':
        first_name=request.POST.get('firstname','')
        last_name=request.POST.get('lastname','')
        username = request.POST.get('username', '')
        mail=request.POST.get('email','')
        password=request.POST.get('password','')
        confirm_pass=request.POST.get('confirm_password','')
        gender=request.POST.get('gender','')
        phone=request.POST.get('phone','')


        # Checking for duplicate users

        userCheck = User.objects.filter(username=username) | User.objects.filter(email=mail)

        if userCheck:
            messages.error(request, "already taken")
            return redirect('/')

        # Checking for confirm passowrds

        if password != confirm_pass:
            return HttpResponse("Password does not match")
            return redirect('/')      
      
        if password==confirm_pass:
            user_obj = User.objects.create_user(first_name = first_name, last_name=last_name, password=password, email = mail, username=username)
            user_obj.save()
            return redirect('/login') 
        else: messages.error(request, "There is no user exist with those credetials")
    return redirect('/') 


def user_login(request):
 
    if request.method=='POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

       # if user account exist or not

        user  = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            
            return HttpResponse("Logged in")
        else:
           return HttpResponse("Invalid credentials")   

    else:
        return render(request, 'account/login.html')


def user_logout(request):
    user_logout(request)
    messages.success(request, "logged out")
    return redirect("/")








