from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from ..models import Tank
from ..serializers import PHHistorySerializer

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
