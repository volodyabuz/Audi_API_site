from django import template
from audiapi.models import *
import requests


register = template.Library()

@register.inclusion_tag('webapp/cars.html')
def somecars():
    """Вывод трех программ занятий школы."""
    r = requests.get('http://127.0.0.1:8000/api/v1/audi/')
    json_response = r.json()
    qsetq = json_response['results']
    print(qsetq)
    for i in qsetq:
        print(i['car_photo'])
    qset = Cars.objects.filter(pk__lte=4)
    print(qset)

    return {
        'qset': qsetq,
    }
