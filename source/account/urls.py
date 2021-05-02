from django.contrib import admin
from django.urls import path
from account import views
from django.contrib.auth import views as auth_views

urlpatterns = [

    path('', views.home, name='home'),

    path('homapge', views.homepage, name='homepage'),

    path('signup', views.signup, name='signup'),

    path('user_login', views.user_login, name='user_login'),

    path('user_logout', views.user_logout, name='user_logout'),

    path('reset_password', auth_views.PasswordResetView.as_view(template_name="account/reset_password.html"), name="reset_password"),

    path('reset_password_sent', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),

    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="account/reset.html"), name="password_reset_complete"),
   
]
