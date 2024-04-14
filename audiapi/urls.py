from django.contrib import admin
from django.urls import path, include, re_path
from .views import *
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView


router_audi = routers.DefaultRouter()
router_audi.register(r'audi', AudiViewSet)


urlpatterns = [
    path('api/v1/', include(router_audi.urls)),
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    path('api/v1/usergarage/', UserGarageAPIList.as_view()),
    path('api/v1/usergarage/<int:pk>/', UserGarageAPIChange.as_view()),
    path('api/v1/commentlist/', CommentAPIList.as_view()),
    path('api/v1/commentlist/<int:car_id>/', CommentAPIListByCar.as_view()),
    path('get-model-car-list/<int:user_id>/', AudiViewSet.as_view({'get': 'retrieve'}), name='get-model-car-list'),
    # path('api/v1/auth/', include('djoser.urls')),
    # re_path(r'^auth/', include('djoser.urls.authtoken')),

    # path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('api/v1/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    # path('api/v1/audilist/', AudiViewSet.as_view({'get': 'list'})),
    # path('api/v1/audilist/<int:pk>/', AudiViewSet.as_view({'get': 'retrieve', 'put': 'update'})),
]
