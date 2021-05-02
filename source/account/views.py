from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from account.models import User
from django.contrib.auth import authenticate, login
from django.contrib.admin import forms
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from django.contrib.auth import logout as django_logout
from django.http import HttpResponseRedirect
import requests
import json






# Create your views here.


def home(request):

    """
    This function renders the home page of our website. Which is create an account by default

    """


    return render(request, 'account/signup.html')


def homepage(request):

    """
    This function renders the home page of our website. Which is create an account by default

    """


    return render(request, 'homepage/home.html')

@csrf_protect
def user_login(request):

    """
    This function is for user login and google recapthcha. It will check if the user is registerted or not.
    This function will also make sure if you are not a robot. After that it will try to log in with credentials.

    """


 
    if request.method=='POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        clientkey=request.POST['g-recaptcha-response']
        secretkey='6Le2zcAaAAAAADgul2ChuQHbvXycZhapt0UwBZ-7'

        capthchaData ={
            'secret': secretkey,
            'response': clientkey
        }
        r= requests.post('https://www.google.com/recaptcha/api/siteverify', data=capthchaData)
        response=json.loads(r.text)
        verify= response['success']
        print('Your success is :', verify)

            
            
            
        if verify:
            user  = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
            
                return redirect("homepage")
            else:
                messages.error(request, "Invalid credentials")
                return render(request, 'account/login.html')

        else:


                messages.error(request, "Please make sure you are not a robot!")
                return render(request, 'account/login.html')
    
    
    else:
        return render(request, 'account/login.html')
      

        



def user_logout(request):

    """
    This function is for user logout.

    """

    django_logout(request)
    messages.success(request, "logged out")
    return redirect("/user_login")


def signup(request): 

    """
    This function is for user signup. User will get values from form and will check if username or
    email is already registerted or not. Then it will create a user object and save it.

    """


    if request.method =='POST':
        first_name=request.POST.get('firstname', '')
        last_name=request.POST.get('lastname', '')
        username = request.POST.get('username', '')
        mail=request.POST.get('email', '')
        password=request.POST.get('password', '')
        confirm_pass=request.POST.get('confirm_password', '')
       

        # Checking for duplicate users

        userCheck = User.objects.filter(username = username) | User.objects.filter(email = mail)

        if  userCheck:
            messages.error(request, "username or email already taken")
            return redirect('/')

        # Checking for confirm passowrds

        if password != confirm_pass:
            messages.error(request, "Password and Confirm password does not match! ")
            return redirect('/')      
      
        if password==confirm_pass:
            user_obj = User.objects.create_user(first_name = first_name, last_name=last_name, password=password, email = mail, username=username)
            user_obj.save()
            return redirect('/user_login') 
        
        else: messages.error(request, "There is no user exist with those credetials")
    
    return redirect('/') 



