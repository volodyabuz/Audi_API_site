from django.shortcuts import render
from audiapi.models import *

nav_item = {
    '': 'Главная',
    'catalog': 'Каталог',
    'review': 'Отзывы',
    'contact': 'Контакты',
}
context = {
    'nav_item': nav_item,
}

def index(request):
    context['title'] = 'Главная'
    return render(request, 'webapp/index.html', context=context)

def about(request):
    return render(request, 'webapp/contact.html')