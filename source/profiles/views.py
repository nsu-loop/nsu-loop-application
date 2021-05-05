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
