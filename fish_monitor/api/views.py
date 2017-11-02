from django.http import HttpResponse
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Tank
from .serializers import TankSerializer
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
