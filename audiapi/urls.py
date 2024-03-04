from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', get_car_model_list, name='home'),
    # path('get-model-car-list/<int:car_id>/', get_car_model_list, name='get-model-car-list'),
    path('api/v1/audilist/', AudiAPIView.as_view()),
    path('api/v1/audilist/<int:pk>/', AudiAPIView.as_view()),
]
