import random
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.db.models import Q
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect, get_object_or_404
from django.template.defaultfilters import first, last
from django.views.generic import ListView, DetailView

from .forms import ProfileModelForm
from .models import Profile, Skill


# function for displaying my profile
@login_required
def my_profile_view(request):
    """
    This method creates the view of my-profile and post request of update my profile.
    It will update the profile form and show the profile data.
    This method only work for logged in user.

    :param name: request - it generates the response(HTTP)
    :param type: HttpResponse
    :return: returns the profile view
    """
    profile = Profile.objects.get(user=request.user)
    form = ProfileModelForm(request.POST or None, request.FILES or None, instance=profile)
    confirm = False

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            confirm = True

    context = {
        'profile': profile,
        'form': form,
        'confirm': confirm,
    }

    return render(request, 'profiles/myprofile.html', context)


# function for displaying friend profile
def friend_profile_view(request, userId):
    """
    This method returns the view of friend profile
    It is open for any profile

    :param name: request - it generates the response(HTTP)
    :param type: HttpResponse
    :return: returns the profile view
    :param name: userId - It contains the userId of requested user
    :param type: Int
    :return: returns the profile view
    """

    profile = Profile.objects.get(pk=userId)
    context = {
        'profile': profile
    }
    return render(request, 'profiles/myprofile.html', context)


# function for talent poll rednering
def talent_poll(request):
    """
    This method creates the view of talent poll.
    This method only work for logged in user.

    :param name: request - it generates the response(HTTP)
    :param type: HttpResponse
    :return: returns the talent poll view
    """
    # retrieving all skills and select one randomly
    skills = Skill.objects.all()
    skill_index = random.sample(range(0, len(skills)), 1)[0]

    # retrieving all profiles and select 5 randomly
    friends = Profile.objects.all()
    # default choice is 5
    choice_number = 5
    # but if total friend is less than 5, the choice number becomes total friend number
    if len(friends) < 5:
        choice_number = len(friends)
    friend_indexes = random.sample(range(0, len(friends)), choice_number)
    friends = [friends[i] for i in friend_indexes]

    context = {
        'skill': skills[skill_index].name,
        'friends': friends
    }

    return render(request, 'profiles/talent_poll.html', context)


# function for saving talent poll vote
def save_talen_poll(request, skill, userId):
    """
    This method creates the view of talent poll.
    This method only work for logged in user.

    :param name: request - it generates the response(HTTP)
    :param type: HttpResponse
    :param name: skill - It contains the saved skill
    :param type: String
    :param name: userId - It contains the userId of requested user
    :param type: Int
    :return: returns the profile view
    """

    # retrieving user and corresponding profile based on userId
    user = User.objects.get(pk=userId)
    profile = Profile.objects.get(user=user)

    # updating skill
    # if no skill exists
    if profile.skills is None:
        profile.skills = {skill: 1}
    # if any skill already exists
    else:
        # updating existing skill
        if skill in profile.skills:
            profile.skills[skill] += 1
        # creating new skill
        else:
            profile.skills[skill] = 1

    # saving profile
    profile.save()

    # redirecting to post page
    return redirect("/profiles/profile/{user.id}")
