import io
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from .models import Cars


# class AudiModel:
#     def __init__(self, name_id, generation_id):
#         self.name_id = name_id
#         self.generation_id = generation_id




class AudiSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name_id = serializers.IntegerField()
    generation_id = serializers.IntegerField()
    body_type_id = serializers.IntegerField()
    fuel_type_id = serializers.IntegerField()
    motor_id = serializers.IntegerField()
    gearbox_id = serializers.IntegerField()
    wheel_drive_id = serializers.IntegerField()
    about = serializers.CharField(read_only=True)
    car_photo = serializers.ImageField(read_only=True)

    def create(self, validated_data):
        return Cars.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        id = serializers.IntegerField()
        instance.name_id = validated_data.get('name_id', instance.name_id)
        instance.generation_id = validated_data.get('generation_id', instance.generation_id)
        instance.body_type_id = validated_data.get('body_type_id', instance.body_type_id)
        instance.fuel_type_id = validated_data.get('fuel_type_id', instance.fuel_type_id)
        instance.motor_id = validated_data.get('motor_id', instance.motor_id)
        instance.gearbox_id = validated_data.get('gearbox_id', instance.gearbox_id)
        instance.wheel_drive_id = validated_data.get('wheel_drive_id', instance.wheel_drive_id)
        instance.about = validated_data.get('about', instance.about)
        instance.car_photo = validated_data.get('car_photo', instance.car_photo)
        instance.save()
        return instance


# def encode():
#     model = AudiModel(3, 1)
#     model_sr = AudiSerializer(model)
#     print(model_sr.data, type(model_sr.data), sep='\n')
#     json = JSONRenderer().render(model_sr.data)
#     print(json)

# def decode():
#     stream = io.BytesIO(b'{"name_id":3,"generation_id":1}')
#     data = JSONParser().parse(stream)
#     serializer = AudiSerializer(data=data)
#     serializer.is_valid()
#     print(serializer.validated_data)