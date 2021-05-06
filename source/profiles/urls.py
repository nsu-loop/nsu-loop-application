from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import (
    my_profile_view,
    friend_profile_view,
    talent_poll,
    save_talen_poll,
)

app_name = 'profiles'

urlpatterns = [
    path('myprofile/', my_profile_view, name='my-profile-view'),
    path('profile/<int:userId>', friend_profile_view, name='friend-profile-view'),
    path("tpoll", talent_poll, name="talent-poll"),
    path("tpoll/<str:skill>/<int:userId>", save_talen_poll, name="talent-poll-vote")

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)