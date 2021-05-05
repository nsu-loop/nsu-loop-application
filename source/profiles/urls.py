from django.urls import path

from .views import (
    my_profile_view,
    friend_profile_view
)

app_name = 'profiles'

urlpatterns = [
    path('myprofile/', my_profile_view, name='my-profile-view'),
    path('profile/<int:userId>', friend_profile_view, name='friend-profile-view')
]
