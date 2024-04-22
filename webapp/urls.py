from django.contrib import admin
from django.urls import path, include, re_path
from .views import *


urlpatterns = [
    path('', index, name='home'),
    path('contact/', about, name='contact'),
    path('catalog/', Catalog.as_view(), name='catalog'),
    path('review/', review, name='review'),
]
