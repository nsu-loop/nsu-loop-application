from django.contrib.auth.models import User
from django.db.models.query import QuerySet
from django.shortcuts import redirect, render
from django.template.defaultfilters import first, last
from .models import Skill
from posts.models import *
from posts.forms import *
from profiles.forms import *
import random

# function for displaying friend profile
def friend_profile_view(request, userId):
    """
    This method will display friend profile.

    :param name: request - used to generate responses(Http) depending on the request that it receives
    :param type: HttpResponse
    :param name: userId - used to take the user id
    :param type: HttpResponse
    :return: returns myprofile page
    
    """
    profile = Profile.objects.get(pk=userId)
    context = {
        'profile': profile
    }
    return render(request, 'profiles/myprofile.html', context)


# function for rendering  find page
def find_view(request):
    """
    This method will render find page.

    :param name: request - used to generate responses(Http) depending on the request that it receives
    :param type: HttpResponse
    :return: returns find page
    
    """
    return render(request, 'profiles/find.html')

# function for rendering find post page
def search_post(request):
    """
    This method will render find post page.

    :param name: request - used to generate responses(Http) depending on the request that it receives
    :param type: HttpResponse
    :return: returns find post page
    
    """
    # getting search text from url
    search_text = request.GET.get('text', None)
    if search_text is None:
        search_text = ""

    posts = Post.objects.filter(content__contains=search_text)

    # reused from post view
    c_form = CommentModelForm()

    profile = Profile.objects.get(user=request.user)

    if 'submit_c_form' in request.POST:
        c_form = CommentModelForm(request.POST)
        if c_form.is_valid():
            instance = c_form.save(commit=False)
            instance.user = profile
            instance.post = Post.objects.get(id=request.POST.get('post_id'))
            instance.save()
            c_form = CommentModelForm()

    context = {
        'search_text': search_text,
        'qs': posts,
        'profile': profile,
        'c_form': c_form,
    }

    return render(request, 'profiles/search_posts.html', context)

# function for searching people
def search_friends(request):
    """
    This method functionality is searching people.

    :param name: request - used to generate responses(Http) depending on the request that it receives
    :param type: HttpResponse
    :return: returns search_friends page
    
    """
    # getting input values from request
    name = request.GET.get('name', "")
    email = request.GET.get('email', "")
    phone = request.GET.get("phone", "")
    cgpa = request.GET.get("cgpa", "")
    grad_year = request.GET.get("grad_year", "")
    major = request.GET.get("major", "")

    # if we got input from the form then based on each property
    # filtering profiles
    friends = Profile.objects.none() # initially we assumes that no user found, this assumption is for OR condition
    if len(name) > 0:
        friends = friends | Profile.objects.filter(first_name__contains=name) | Profile.objects.filter(last_name__contains=name)
    if len(email) > 0:
        friends = friends | Profile.objects.filter(email=email)
    if len(phone) > 0:
        friends = friends | Profile.objects.filter(phone=phone)

    # if no friend found based on first three fields
    # then search based on the other properties
    if len(friends) == 0:
        friends = Profile.objects.all() # initially we assumes all user found, this assumption is based on AND assumption
        if len(cgpa) > 0:
            friends = friends & Profile.objects.filter(cgpa=cgpa)
        if len(grad_year) > 0:
            friends = friends & Profile.objects.filter(grad_year=grad_year)
        if len(major) > 0:
            friends = friends & Profile.objects.filter(major__contains=major)
    
    # in search default all frind name will be listed
    # so makeing the list empty here
    if len(friends) == len(Profile.objects.all()):
        friends = Profile.objects.none()

    # checking wheather the result is empty or not
    empty_result = False
    if (len(name) or len(email) or len(phone) or len(cgpa) or len(grad_year) or len(major) ) and len(friends) == 0:
        empty_result = True

    context = {
        'name': name,
        'email': email,
        'phone': phone,
        'cgpa': cgpa,
        'grad_year': grad_year,
        'major': major,
        'empty_result': empty_result,
        'friends': friends
    }

    return (render(request, 'profiles/search_friends.html', context))

# function for talent poll rednering
def talent_poll(request):
    """
    This method functionality is talent poll rednering.

    :param name: request - used to generate responses(Http) depending on the request that it receives
    :param type: HttpResponse
    :return: returns talent_poll page
    
    """
    # retrieving all skills and select one randomly
    skills = Skill.objects.all()
    skill_index = random.sample(range(0, len(skills)), 1)[0]

    # retrieving all profiles and select 5 randomly
    friends = Profile.objects.all()
    # default choice is 5
    choice_number = 5
    # but if total friend is less than 5, the choice number becomes total friend number.
    if len(friends) < 5:
        choice_number = len(friends)
    friend_indexes = random.sample(range(0, len(friends)), choice_number)
    friends = [friends[i] for i in friend_indexes]

    context = {
        'skill': skills[skill_index].name,
        'friends': friends
    }

    return render(request, 'profiles/talent_poll.html', context)