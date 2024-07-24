from celery import shared_task
from .parser import *


@shared_task
def send_adds_to_user():
    url = "https://auto.drom.ru/audi/a4/generation5/restyling1/"
    print(fresh_six_ads(url))
    print(avg_price(url))