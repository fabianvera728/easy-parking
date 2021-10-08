# Django restframework
from rest_framework import mixins, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import filters

from django.db.models import Count

# Models
from easy_parking.parking_lots.models.parking_lots import Parking
from easy_parking.reservations.models.reservations import Reservation
from easy_parking.reservations.models.places import Place

# Serializers
from easy_parking.parking_lots.serializers.parking_lots import ParkingSerializer
from easy_parking.reservations.serializers.reservations import ReservationSerializer
from easy_parking.reservations.serializers.places import PlaceSerializer


class Parkings(mixins.CreateModelMixin,
               mixins.RetrieveModelMixin,
               mixins.UpdateModelMixin,
               mixins.ListModelMixin,
               viewsets.GenericViewSet):
    serializer_class = ParkingSerializer
    queryset = Parking.objects.all()

    lookup_field = 'slug_name'
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['^slug_name', '^description', '^name']
    ordering_fields = ['slug_name', 'name', 'reputation', 'price__morning',
                       'price__morning', 'price__evening',
                       'price__night', 'price__weekend']


    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        for p in serializer.data:
            places = Place.objects.filter(parking=p['id'])
            p['places'] = PlaceSerializer(places, many=True).data
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        places = Place.objects.filter(parking=instance)
        print(places, serializer.data['places'], 'wilmer\n')
        serializer.data['places'] = PlaceSerializer(places, many=True).data
        print(serializer.data['places'], 'wilmer\n')
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def reservations(self, request, *args, **kwargs):
        reservations = Reservation.objects.filter(parking=self.get_object())
        serializer = ReservationSerializer(reservations, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def places(self, request, *args, **kwargs):
        places = Place.objects.filter(parking=self.get_object())
        serializer = PlaceSerializer(places, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def top(self, request, *args, **kwargs):
        parkings = Parking.objects.all().order_by('-reputation')[:10]
        serializer = ParkingSerializer(parkings, many=True)
        return Response(serializer.data)
