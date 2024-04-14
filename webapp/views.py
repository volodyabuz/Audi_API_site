from django.shortcuts import render

def index(request):
    return render(request, 'webapp/index.html', context={"title": 'Главная'})

def about(request):
    return render(request, 'webapp/contact.html')