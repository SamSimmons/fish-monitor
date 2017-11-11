from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault
from .models import Tank, WaterChangeHistory, TempHistory, PHHistory
from django.contrib.auth import get_user_model

UserModel = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = UserModel
        fields = (
            'username',
            'email',
            'password',
        )

    def create(self, validated_data):
        print("->", UserModel)
        user = UserModel.objects.create(
            username = validated_data['username'],
            email = validated_data['email']

        )
        user.set_password(validated_data['password'])
        user.save()
        return user


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

class PHHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PHHistory
        fields = ('tank_id', 'modified_date', 'ph')
