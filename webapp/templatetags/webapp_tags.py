from django import template
from audiapi.models import *
import requests
from audiapisite.settings import ALLOWED_HOSTS


register = template.Library()

@register.inclusion_tag('webapp/cars.html')
def somecars():
    """Вывод четырех моделей авто."""
    r = requests.get(f'http://{ALLOWED_HOSTS[0]}:8000/api/v1/audi/')
    json_response = r.json()
    qsetq = json_response['results']

    return {
        'qset': qsetq,
    }
