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


class AudiAPIList(generics.ListCreateAPIView):
    queryset = Cars.objects.all()
    serializer_class = AudiSerializer


class AudiAPIUpdate(generics.UpdateAPIView):
    queryset = Cars.objects.all()
    serializer_class = AudiSerializer


class AudiAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cars.objects.all()
    serializer_class = AudiSerializer

# class AudiAPIView(APIView):

#     def get(self, request, *args, **kwargs):
#         pk = kwargs.get('pk', None)
#         if pk:
#             try:
#                 instance = Cars.objects.get(pk=pk)
#                 return Response({'posts': AudiSerializer(instance).data})
#             except:
#                 return Response({'error': 'Object does not exist'})
#         lst = Cars.objects.all()
#         return Response({'posts': AudiSerializer(lst, many=True).data})

    
#     def post(self, request):
#         serializer = AudiSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()

#         return Response({'new_car': serializer.data})

#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get('pk', None)
#         if not pk:
#             return Response({'error': 'Method PUT is not allowed'})
        
#         try:
#             instance = Cars.objects.get(pk=pk)
#         except:
#             return Response({'error': 'Object does not exist'})

#         serializer = AudiSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({'changed_car': serializer.data})
    
#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get('pk')
#         if not pk:
#             return Response({'error': 'Method DELETE is not allowed'})
        
#         try:
#             temp = Cars.objects.get(pk=pk)
#         except:
#             return Response({'error': 'Object does not exist'})
#         temp.delete()
#         return Response({'deleted_item': AudiSerializer(temp).data})
