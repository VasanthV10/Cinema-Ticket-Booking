"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import include,url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('cinema.urls')),
    path('cinema/',include('cinema.urls')),
    #path('payment/',include('payment.urls')),
    path('seat/',include('seats.urls')),
    path('times/',include('times.urls')),
    path('signout',include('login.urls')),
    path('aboutus/',include('aboutus.urls')),
    path('contact/',include('contact.urls')),
    path('knowmore/',include('desc.urls')),
    path('login/',include('login.urls')),
    path('register/',include('register.urls')),
    path('movieregistration/',include('moviereg.urls')),
    path('portal/',include('regportal.urls')),
    path('Moviehomepage/',include('movhome.urls')),
    path('userprofile/',include('userprofile.urls')),
]
