from django.http import Http404
from dateutil import parser
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from ..models import Tank
from ..serializers import TankSerializer, WaterChangeHistorySerializer

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
