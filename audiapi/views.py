from django.forms.models import model_to_dict
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets

from .forms import CarForm

from .models import *
from .serializers import AudiSerializer

def get_car_model_list(request):
    car_list = CarModels.objects.all()
    model_car_list = Generations.objects.select_related('model_name')

    context = {'title': 'Главная', 'car_list': car_list, 'model_car_list': model_car_list}
    return render(request, 'audiapi/index.html', context=context)


class AudiViewSet(viewsets.ModelViewSet):
    queryset = Cars.objects.all()
    serializer_class = AudiSerializer


# class AudiAPIList(generics.ListCreateAPIView):
#     queryset = Cars.objects.all()
#     serializer_class = AudiSerializer


# class AudiAPIUpdate(generics.UpdateAPIView):
#     queryset = Cars.objects.all()
#     serializer_class = AudiSerializer


# class AudiAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Cars.objects.all()
#     serializer_class = AudiSerializer

