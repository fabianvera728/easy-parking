# Django restframework
from rest_framework import mixins, viewsets

# Models
from easy_parking.users.models.vehicles import Vehicle

# Serializers
from easy_parking.users.serializers.vehicles import VehicleSerializer


class Vehicles(mixins.CreateModelMixin,
               mixins.RetrieveModelMixin,
               mixins.UpdateModelMixin,
               mixins.ListModelMixin,
               viewsets.GenericViewSet):
    serializer_class = VehicleSerializer
    queryset = Vehicle.objects.all()
