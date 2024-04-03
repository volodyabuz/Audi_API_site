from django.contrib import admin
from django.urls import path, include
from .views import *
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'audi', AudiViewSet)
print(router.urls)

urlpatterns = [
    path('', get_car_model_list, name='home'),
    path('api/v1/', include(router.urls)),
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    path('api/v1/usergarage/', UserGarageAPIList.as_view()),
    path('api/v1/usergarage/<int:pk>/', UserGarageAPIChange.as_view()),
    path('get-model-car-list/<int:pk>/', AudiViewSet.as_view({'get': 'retrieve'}), name='get-model-car-list'),
    # path('api/v1/audilist/', AudiViewSet.as_view({'get': 'list'})),
    # path('api/v1/audilist/<int:pk>/', AudiViewSet.as_view({'get': 'retrieve', 'put': 'update'})),
]
