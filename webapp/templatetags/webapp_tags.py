from django import template
from audiapi.models import *
import requests
from audiapisite.settings import ALLOWED_HOSTS


register = template.Library()


@register.simple_tag(name='distincts')
def distinct_values(filter=None):
    if not filter:
        q = requests.get(f'http://{ALLOWED_HOSTS[0]}:8000/api/v1/audi/')
        json_response = q.json()
        return json_response['results']
    else:
        q = requests.get(f'http://{ALLOWED_HOSTS[0]}:8000/api/v1/audi/?distinct={filter}')
        json_response = q.json()
        print(json_response['results'])
        return json_response['results']


@register.inclusion_tag('webapp/cars.html')
def somecars():
    """Вывод четырех моделей авто."""
    # r = requests.get(f'http://{ALLOWED_HOSTS[0]}:8000/api/v1/audi/')
    # json_response = r.json()
    # qsetq = json_response['results']
    qsetq = distinct_values('generation')

    return {
        'qset': qsetq,
    }
