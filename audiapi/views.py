from django.forms.models import model_to_dict
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.pagination import PageNumberPagination

from .models import *
from .serializers import *
from .permissions import *


class AudiAPIListPagination(PageNumberPagination):
    page_size = 4
    page_size_query_param = 'page_size' #для ввода в параметры запорса &page_size=4 и изменения пагинации http://127.0.0.1:8000/api/v1/audi/?page=2&page_size=4
    max_page_size = 10000 #но не более данного значения


class AudiViewSet(viewsets.ModelViewSet):
    queryset = Cars.objects.all()
    serializer_class = AudiSerializer
    permission_classes = (IsAdminOrReadOnly, )
    pagination_class = AudiAPIListPagination


    def get_queryset(self):
        distinct = self.request.query_params.get('distinct') #Поиск уникальных значений
        if distinct is not None:
            return Cars.objects.order_by().distinct(distinct)

        pk = self.kwargs.get('pk')
        if not pk:
            return Cars.objects.all()
        return Cars.objects.filter(pk=pk) #Из-за того, что queryset получает СПИСОК, то метод FILTER, а не GET

    @action(methods=['get'], detail=True)
    def bodytype(self, request, pk=None):
        body = BodyTypes.objects.get(pk=pk)
        return Response({'bodies': body.body})


class UserGarageAPIList(generics.ListCreateAPIView):
    queryset = Garage.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    # authentication_classes = (TokenAuthentication, )

    def list(self, request):
        if request.user.is_authenticated:
            queryset = Garage.objects.filter(user_id=request.user.id)
        else:
            queryset = self.get_queryset()
        if request.user.is_superuser:
            queryset = Garage.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)


class UserGarageAPIChange(generics.RetrieveUpdateDestroyAPIView):
    queryset = Garage.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsOwnerOrAdmin, )
    # authentication_classes = (TokenAuthentication, )

    # def filter_queryset(self, queryset):
    #     print(request.user.id)
    #     queryset = Garage.objects.filter(user=request.user.id)
    #     serializer = UserSerializer(queryset, many=False)
    #     return Response(serializer.data)


class CommentAPIList(generics.ListAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer


class CommentAPIListByCar(generics.ListCreateAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )

    def get_queryset(self):
        car_id = self.kwargs.get('car_id')
        if not car_id:
            return Comments.objects.all()
        return Comments.objects.filter(car_id=car_id)

