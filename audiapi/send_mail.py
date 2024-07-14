from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.shortcuts import redirect, render
from .parser import *


def send_email_func(ad_list, subject_mail, address):
    '''Отправляет контекст на почту (привязана к шаблону email.html).'''

    # Формируем шаблон пиьсма
    html_body = render_to_string('audiapi/email.html', context={'data': ad_list})
    # Отправляем пиьсмо
    msg = EmailMultiAlternatives(
        subject=f'Audi API: {subject_mail}',
        to=[address]
    )
    msg.attach_alternative(html_body, "text/html")
    msg.send()

    return redirect('home')
