"""tavelbuddy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from user_interface.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index.as_view(),name="index"),
    path('login/',login.as_view(),name="login"),
    path('signup/',signup.as_view(),name="signup"),
    path('user_profile/<str:name>/', user_profile.as_view(), name='user_profile'),
    path('plantrip/',plantrip.as_view(),name="plantrip"),
    path('mytrips/',mytrips,name="mytrips"),
    path('tipsuggestion/',tripsuggestions.as_view(),name="tripsuggestions")
]
