# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from rest_framework import generics
from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import status
from .models import Tank, Fish
from .serializers import TankSerializer, FishSerializer
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly

class TankList(generics.ListCreateAPIView):
    queryset = Tank.objects.all()
    serializer_class = TankSerializer
    permission_classes = (IsAdminOrReadOnly, )

class TankDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tank.objects.all()
    serializer_class = TankSerializer
    permission_classes = (IsAdminOrReadOnly, )
    lookup_url_kwarg = 'tank_id'

class FishList(generics.ListCreateAPIView):
    queryset = Fish.objects.all()
    serializer_class = FishSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

    def perform_create(self, serializer):
        serializer.save(
            created_by=self.request.user,
            tank_id=self.kwargs['pk']
        )

class FishDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = FishSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
    lookup_url_kwarg = 'fish_id'

    def get_queryset(self):
        fish = self.kwargs['fish_id']
        return Fish.objects.filter(id=fish)
