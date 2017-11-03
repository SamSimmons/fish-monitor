from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault
from .models import Tank, WaterChangeHistory, TempHistory

class TankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tank
        fields = (
            'owner',
            'name',
            'last_water_change',
            'water_change_freq',
            'last_temp',
            'temp_min',
            'temp_max',
            'last_ph',
            'ph_min',
            'ph_max',
            'last_ammonia',
            'ammonia_min',
            'ammonia_max',
            'light_value',
        )

class WaterChangeHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = WaterChangeHistory
        fields = ('tank_id', 'modified_date')

class TempHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TempHistory
        fields = ('tank_id', 'modified_date', 'temperature')
