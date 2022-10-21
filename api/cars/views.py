from rest_framework import viewsets, status
from rest_framework.response import Response

from api.cars.serializers import CarSerializer
from cars.models import Car


class CarViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows posts to be viewed.
    """

    queryset = Car.objects.all().order_by("-created_at")
    serializer_class = CarSerializer
    permission_classes = []

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        Car.objects.create(**serializer.validated_data)
        return Response(status=status.HTTP_201_CREATED)
