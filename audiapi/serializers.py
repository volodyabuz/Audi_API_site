from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from .models import *


class AudiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cars
        # fields = ('name', 'generation')
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Garage
        fields = "__all__"
