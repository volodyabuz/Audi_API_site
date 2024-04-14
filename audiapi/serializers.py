from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from .models import *


class AudiSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='name.car_name')
    generation = serializers.CharField(source='generation.gen')
    body_type = serializers.CharField(source='body_type.body')
    fuel_type = serializers.CharField(source='fuel_type.fuel')
    motor = serializers.CharField(source='motor.engine')
    gearbox = serializers.CharField(source='gearbox.gear')
    wheel_drive = serializers.CharField(source='wheel_drive.wd')
    class Meta:
        model = Cars
        # fields = ('name', 'generation')
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Garage
        fields = "__all__"

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = "__all__"
