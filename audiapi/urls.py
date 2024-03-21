from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', get_car_model_list, name='home'),
    # path('get-model-car-list/<int:car_id>/', AudiAPIList.as_view(), name='get-model-car-list'),
    path('api/v1/audilist/', AudiAPIList.as_view()),
    path('api/v1/audilist/<int:pk>/', AudiAPIUpdate.as_view()),
    path('api/v1/audidetail/<int:pk>/', AudiAPIDetailView.as_view()),
]
