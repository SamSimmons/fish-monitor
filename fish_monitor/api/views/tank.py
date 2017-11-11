from django.http import Http404
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from ..models import Tank
from ..serializers import TankSerializer
from ..permissions import IsAdminOrReadOnly

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
    def get(self, request, pk, format=None):
        tank = self.get_object(pk)
        serializer = TankSerializer(tank)
        return Response(serializer.data)
