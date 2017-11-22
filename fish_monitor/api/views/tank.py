from django.http import Http404
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from ..models import Tank, WaterChangeHistory, TempHistory
from ..serializers import TankSerializer, WaterChangeHistorySerializer, TempHistorySerializer
from ..permissions import IsAdminOrReadOnly
from datetime import datetime, timedelta
import json
from django.utils import timezone

class TankList(generics.ListCreateAPIView):
    queryset = Tank.objects.all()
    serializer_class = TankSerializer
    permission_classes = (IsAdminOrReadOnly, )

    def get_tanks(self, id):
        try:
            return Tank.objects.filter(owner=id)
        except Tank.DoesNotExist:
            raise Http404

    def post(self, request, format=None):
        data = request.data
        data['owner'] = request.user.id
        data['last_water_change'] = datetime.fromtimestamp(float(data['last_water_change']) / 1000.0)
        serializer = TankSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):
        owner = request.user.id
        data = self.get_tanks(owner)
        serializer = TankSerializer(data, many=True)
        return Response(serializer.data)


class TankDetail(APIView):
    def get_object(self, pk):
        try:
            return Tank.objects.get(pk=pk)
        except Tank.DoesNotExist:
            raise Http404

    def get_water_changes(self, id):
        cutoff = timezone.now() - timedelta(days = 14)
        return WaterChangeHistory.objects.filter(tank=id).filter(modified_date__gte = cutoff)

    def get_temp_history(self, id):
        cutoff = timezone.now() - timedelta(days = 14)
        return TempHistory.objects.filter(tank=id).filter(modified_date__gte = cutoff)

    def merge_details(self, tank, changes, temps):
        return { 'tank': tank, 'changes': changes, 'temps': temps }

    def get(self, request, pk, format=None):
        tank = self.get_object(pk)
        if tank.id == request.user.id:
            serializer = TankSerializer(tank)

            changes = self.get_water_changes(tank.id)
            changes_serializer = WaterChangeHistorySerializer(changes, many = True)

            temps = self.get_temp_history(tank.id)
            temp_serializer = TempHistorySerializer(temps, many = True)

            data = self.merge_details(serializer.data, changes_serializer.data, temp_serializer.data)
            return Response(data)
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    def delete(self, request, pk, format=None):
        tank = self.get_object(pk)
        if tank.id == request.user.id:
            tank.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_401_UNAUTHORIZED)
