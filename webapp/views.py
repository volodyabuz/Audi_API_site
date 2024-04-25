from typing import Any, Dict
from django.db.models.query import QuerySet
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
import requests
from audiapi.models import *
from audiapisite.settings import ALLOWED_HOSTS

nav_item = [
    {'title': 'Главная', 'url_name': 'home'},
    {'title': 'Каталог', 'url_name': 'catalog'},
    {'title': 'Отзывы', 'url_name': 'review'},
    {'title': 'Контакты', 'url_name': 'contact'},
    {'title': 'API', 'url_name': 'api-root'},
]
context = {
    'nav_item': nav_item,
}

def index(request):
    context['title'] = 'Главная'
    return render(request, 'webapp/index.html', context=context)

def about(request):
    context['title'] = 'Контакты'
    return render(request, 'webapp/contact.html', context=context)

def review(reqest):
    return HttpResponse("Обратная связь")


class Catalog(ListView):
    template_name = 'webapp/catalog.html'
    context_object_name = 'cars'

    def get_queryset(self) -> QuerySet[Any]:
        q = requests.get(f'http://{ALLOWED_HOSTS[0]}:8000/api/v1/audi/')
        json_response = q.json()
        qsetq = json_response['results']
        return qsetq
    
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title'] = "Каталог"
        context['nav_item'] = nav_item
        return context
