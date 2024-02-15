from django.http import HttpResponse
from django.shortcuts import render
from .models import *

def index(request):
    return HttpResponse('<h1>eeee</h1>')
