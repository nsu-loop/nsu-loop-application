from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from account.models import UserProfile
from django.contrib.auth import authenticate, login


# Create your views here.


def home(request):
    return render(request, 'account/signup.html')


def user_login(request):
 
    if request.method=='POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

       

        user  = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            
            return HttpResponse("Logged in")
        else:
           return HttpResponse("Invalid")   

    else:
        return render(request, 'account/login.html')

def logout(request):
    logout(request)
    messages.success(request, "logged out")
    return redirect("/")


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

        userCheck = User.objects.filter(username=username) | User.objects.filter(email=mail)

        if userCheck:
            messages.error(request, "already taken")
            return redirect('/')
      
        if password==confirm_pass:
            user = User.objects.create_user(first_name = first_name, last_name=last_name, password=password,email = mail,username=username)
            UserProfile.objects.create(user=user,gender=gender,phone=phone)
            user.save()
        else: messages.error(request, "There is no user exist with those credetials")
    return redirect('/') 



