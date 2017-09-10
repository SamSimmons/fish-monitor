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

class TankWaterChange(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly, )
    def get_object(self, pk):
        try:
            return Tank.objects.get(pk=pk)
        except Tank.DoesNotExist:
            raise Http404
    def post(self, request, tank_id, format=None):
        tank = self.get_object(tank_id)
        serializer = TankSerializer(tank, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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
