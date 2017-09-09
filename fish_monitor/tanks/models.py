# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Tank(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    water_change = models.DateField()

class Fish(models.Model):
    tank = models.ForeignKey(Tank, related_name='fishes')
    name = models.CharField(max_length=255)
    fish_type = models.TextField()
    created_by = models.ForeignKey(User)
