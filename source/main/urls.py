"""
main URL Configuration

The 'urlpatterns' list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/

Examples:

Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))

"""

from django.contrib import admin
from django.urls import path, include
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('payments/', include('payment.urls', namespace='payments')),
    path('finds/', include('find.urls', namespace='finds')),
    path('profiles/', include('profiles.urls', namespace='profiles')),
    path('friendship/', friendship.urls, name="friendship"),
    path('', home_view, name='home-view'),
    path('posts/', include('posts.urls', namespace='posts')),
    path('jackpots/', include('jackpot.urls', namespace='jackpots')),
    path('', include('account.urls'), name='account_app'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
