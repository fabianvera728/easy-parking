# Django restframework
from rest_framework import mixins, viewsets

# Models
from easy_parking.parking_lots.models.addresses import Address

# Serializers
from easy_parking.parking_lots.serializers.addresses import AddressSerializer


class Addresses(mixins.CreateModelMixin,
               mixins.RetrieveModelMixin,
               mixins.UpdateModelMixin,
               mixins.ListModelMixin,
               viewsets.GenericViewSet):
    serializer_class = AddressSerializer
    queryset = Address.objects.all()
