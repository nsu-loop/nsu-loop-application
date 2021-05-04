from django.urls import path
from .views import friend_profile_view, find_view, search_friends, search_post

app_name = 'profiles'

urlpatterns = [
    path("find/", find_view, name="find-view"),
    path("find/posts", search_post, name="search-post"),
    path("find/friends", search_friends, name='search-friends'),
]