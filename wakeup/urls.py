"""wakeup URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from home.views import *


urlpatterns = [
    path('', index, name="home"),
    path('contact.html', contact, name="contact"),
    path('kursy_dla_dzieci.html', kids, name="kids"),
    path('kursy_dla_nastolatkow.html', teens, name="teens"),
    path('kursy_dla_doroslych.html', adults, name="adults"),
    path('wydarzenia.html', events, name="events"),
    path('admin/', admin.site.urls),
]
