from rest_framework import serializers

from .models import Cars

class AudiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cars
        fields = ('name_id', 'generation_id')
