from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault
from .models import Tank

class TankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tank
        fields = ('owner', 'name', 'last_water_change', 'water_change_freq')
