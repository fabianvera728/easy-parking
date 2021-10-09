# Django restframework
from rest_framework import mixins, viewsets

# Models
from easy_parking.parking_lots.models.prices import Price

# Serializers
from easy_parking.parking_lots.serializers.prices import PriceSerializer


class Prices(mixins.CreateModelMixin,
             mixins.RetrieveModelMixin,
             mixins.UpdateModelMixin,
             mixins.ListModelMixin,
             viewsets.GenericViewSet):
    serializer_class = PriceSerializer
    queryset = Price.objects.all()
