from django.db import models
from django.utils import timezone

class Tank(models.Model):
    owner = models.ForeignKey('auth.User')
    name = models.TextField()
    last_water_change = models.DateTimeField(null = True)
    water_change_freq = models.IntegerField(default = 0)
    last_temp = models.DecimalField(max_digits=5, decimal_places=2, default = '0')
    temp_min = models.DecimalField(max_digits=5, decimal_places=2, default = '0')
    temp_max = models.DecimalField(max_digits=5, decimal_places=2, default = '0')
    last_ph = models.CharField(max_length=10, default = '0')
    ph_min = models.CharField(max_length=10, default = '0')
    ph_max = models.CharField(max_length=10, default = '0')
    last_ammonia = models.CharField(max_length=10, null = True)
    ammonia_min = models.CharField(max_length=10, default = '0')
    ammonia_max = models.CharField(max_length=10, default = '0')
    light_value = models.IntegerField(null = True)

class WaterChangeHistory(models.Model):
    tank_id = models.IntegerField()
    modified_date = models.DateTimeField()

class TempHistory(models.Model):
    tank_id = models.IntegerField()
    modified_date = models.DateTimeField(auto_now=True)
    temperature = models.CharField(max_length=10)
