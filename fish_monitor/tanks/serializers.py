from .models import Tank, Fish
from rest_framework import serializers

class FishSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.username')

    class Meta:
        model = Fish
        fields = ('tank', 'name', 'fish_type', 'created_by')

class TankSerializer(serializers.ModelSerializer):
    fishes = FishSerializer(many=True, read_only=True)

    class Meta:
        model = Tank
        fields = ('id', 'name', 'description', 'water_change', 'fishes')
