from django.contrib import admin
from django.urls import path, include, re_path
from .views import *


urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),

]
