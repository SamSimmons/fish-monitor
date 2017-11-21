from django.db import models
from django.utils import timezone

class Tank(models.Model):
    owner = models.ForeignKey('auth.User')
    name = models.TextField()
    size = models.IntegerField(default = 0)
    last_water_change = models.DateTimeField(null = True)
    water_change_freq = models.IntegerField(default = 0)
    last_temp = models.DecimalField(max_digits=5, decimal_places=2, default = '0')
    temp_min = models.DecimalField(max_digits=5, decimal_places=2, default = '0')
    temp_max = models.DecimalField(max_digits=5, decimal_places=2, default = '0')
    last_ph = models.DecimalField(max_digits=5, decimal_places=2, default = '0')
    ph_min = models.DecimalField(max_digits=5, decimal_places=2, default = '0')
    ph_max = models.DecimalField(max_digits=5, decimal_places=2, default = '0')
    last_ammonia = models.DecimalField(max_digits=5, decimal_places=2, default = '0')
    ammonia_max = models.DecimalField(max_digits=5, decimal_places=2, default = '0')
    light_value = models.IntegerField(null = True)
    updated = models.DateTimeField(auto_now=True)

class WaterChangeHistory(models.Model):
    tank = models.ForeignKey(Tank, on_delete=models.CASCADE)
    modified_date = models.DateTimeField()

class TempHistory(models.Model):
    tank = models.ForeignKey(Tank, on_delete=models.CASCADE)
    modified_date = models.DateTimeField(auto_now=True)
    temperature = models.DecimalField(max_digits=5, decimal_places=2)

class PHHistory(models.Model):
    tank = models.ForeignKey(Tank, on_delete=models.CASCADE)
    modified_date = models.DateTimeField(auto_now=True)
    ph = models.DecimalField(max_digits=5, decimal_places=2)
