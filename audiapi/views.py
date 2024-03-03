from django.forms.models import model_to_dict
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from .forms import CarForm

from .models import *
from .serializers import AudiSerializer

def get_car_model_list(request):
    car_list = CarModels.objects.all()
    model_car_list = Generations.objects.select_related('model_name')

    context = {'title': 'Главная', 'car_list': car_list, 'model_car_list': model_car_list}
    return render(request, 'audiapi/index.html', context=context)

# class AudiAPIView(generics.ListAPIView):
#     queryset = Cars.objects.all()
#     serializer_class = AudiSerializer


class AudiAPIView(APIView):

    def get(self, request):
        lst = Cars.objects.all()
        return Response({'posts': AudiSerializer(lst, many=True).data})
    
    def post(self, request):
        serializer = AudiSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        auto_new = Cars.objects.create(
            name_id = request.data['name_id'],
            generation_id = request.data['generation_id'],
            body_type_id = request.data['body_type_id'],
            fuel_type_id = request.data['fuel_type_id'],
            motor_id = request.data['motor_id'],
            gearbox_id = request.data['gearbox_id'],
            wheel_drive_id = request.data['wheel_drive_id'],
            car_photo = 0
        )

        return Response({'new_car': model_to_dict(auto_new)})
