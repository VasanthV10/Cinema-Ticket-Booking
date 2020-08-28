from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from . import views

urlpatterns = [
    path(r'admin/', admin.site.urls),
    url(r'^$', views.index),
    url(r'times/', views.index),
]