from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from ..models import Tank, TempHistory
from ..serializers import TankSerializer, TempHistorySerializer

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
