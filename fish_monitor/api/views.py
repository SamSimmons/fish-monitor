from django.http import HttpResponse, Http404
from dateutil import parser
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Tank, TempHistory
from .serializers import TankSerializer, WaterChangeHistorySerializer, TempHistorySerializer, PHHistorySerializer
from .permissions import IsAdminOrReadOnly

class TankList(generics.ListCreateAPIView):
    queryset = Tank.objects.all()
    serializer_class = TankSerializer
    permission_classes = (IsAdminOrReadOnly, )

    def post(self, request, format=None):
        data = request.data
        data['owner'] = request.user.id
        serializer = TankSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TankDetail(APIView):
    def get_object(self, pk):
        try:
            return Tank.objects.get(pk=pk)
        except Tank.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        tank = self.get_object(pk)
        serializer = TankSerializer(tank)
        return Response(serializer.data)

class WaterChange(APIView):
    def get_object(self, pk):
        try:
            return Tank.objects.get(pk=pk)
        except Tank.DoesNotExist:
            raise Http404
    def post(self, request, pk, format=None):
        tank = self.get_object(pk)
        if tank.owner.id != request.user.id:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        new_date = parser.parse(request.data['water_change'])
        data = { 'last_water_change': new_date }
        tank_serializer = TankSerializer(tank, data=data, partial=True)

        new_history = { 'tank_id': tank.id, 'modified_date': new_date }
        history_serializer = WaterChangeHistorySerializer(data=new_history)
        if tank_serializer.is_valid() and history_serializer.is_valid():
            # everthing is valid, need to save the change date to the table and also add an entry to the change history
            tank_serializer.save()
            history_serializer.save()
            return Response(tank_serializer.data)

        return Response(status=status.HTTP_400_BAD_REQUEST)

class TempReading(APIView):
    def get_object(self, pk):
        try:
            return Tank.objects.get(pk=pk)
        except Tank.DoesNotExist:
            raise Http404
    def validate_temp(self, temp):
        if temp[-1] != 'C' and temp[-1] != 'F':
            return None

        temp_value = float(temp[:-1])
        if temp[-1] == 'F':
            temp_value = ((temp_value - 32) * 5) / 9
        return temp_value

    def get(self, request, pk, format=None):
        tank = self.get_object(pk)
        tank_id = tank.id
        temps = TempHistory.objects.filter(tank_id=tank_id)
        serializer = TempHistorySerializer(temps, many=True)
        return Response(serializer.data)
    def post(self, request, pk, format=None):
        tank = self.get_object(pk)
        if tank.owner.id != request.user.id:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        new_temp = self.validate_temp(request.data['current_temp'])
        if new_temp == None:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        data = { 'last_temp': new_temp }
        tank_serializer = TankSerializer(tank, data=data, partial=True)

        new_history = { 'tank_id': tank.id, 'temperature': new_temp }
        history_serializer = TempHistorySerializer(data=new_history)

        if tank_serializer.is_valid() and history_serializer.is_valid():
            tank_serializer.save()
            history_serializer.save()
            return Response(tank_serializer.data)

        return Response(status=status.HTTP_400_BAD_REQUEST)


class PHReading(APIView):
    def get_object(self, pk):
        try:
            return Tank.objects.get(pk=pk)
        except Tank.DoesNotExist:
            raise Http404
    def validate_ph(self, ph):
        ph_val = float(ph)
        if ph_val >= 0 and ph_val <= 14:
            return ph_val
        return None
    def post(self, request, pk, format=None):
        tank = self.get_object(pk)
        if tank.owner.id != request.user.id:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        new_ph = self.validate_ph(request.data['ph'])
        if new_ph == None:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        data = { 'last_ph': new_ph }
        tank_serializer = TankSerializer(tank, data=data, partial=True)

        new_history = { 'tank_id': tank.id, 'ph': new_ph }
        history_serializer = PHHistorySerializer(data=new_history)

        if tank_serializer.is_valid() and history_serializer.is_valid():
            tank_serializer.save()
            history_serializer.save()
            return Response(tank_serializer.data)

        return Response(status=status.HTTP_400_BAD_REQUEST)
