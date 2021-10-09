# Django restframework
from rest_framework import serializers
from rest_framework.generics import get_object_or_404

# Models
from easy_parking.reservations.models.types import Type

# Serializers
from easy_parking.parking_lots.models.addresses import Address
from easy_parking.parking_lots.models.parking_lots import Parking
from easy_parking.parking_lots.models.prices import Price
from easy_parking.parking_lots.serializers.addresses import AddressSerializer
from easy_parking.parking_lots.serializers.prices import PriceSerializer
from easy_parking.reservations.serializers.places import PlaceSerializer


class ParkingSerializer(serializers.ModelSerializer):
    address = AddressSerializer()
    price = PriceSerializer()
    places = serializers.DictField(allow_null=True)

    class Meta:
        model = Parking
        fields = "__all__"
        read_only_fields = (
            'address',
            'price',
            'places'
        )

    def create(self, validated_data):
        # print(validated_data, 'validated_data\n')
        address_data = validated_data["address"]
        price_data = validated_data["price"]

        places_data = validated_data['places']
        if places_data is not None:
            validated_data.pop('places')

        address = Address.objects.create(**address_data)
        price = Price.objects.create(**price_data)

        validated_data["address"] = address
        validated_data["price"] = price

        parking, created = Parking.objects.update_or_create(**validated_data)
        if created:
            self.create_places(parking, places_data)
        return parking

    def create_places(self, parking, places):
        bus_type = get_object_or_404(Type, pk=places['bus']['type'])
        car_type = get_object_or_404(Type, pk=places['car']['type'])
        motorcycle_type = get_object_or_404(Type, pk=places['motorcycle']['type'])

        validate_data_bus = {
            'type': bus_type,
            'reserved_limit': places['bus']['reserved_limit'],
            'remaining_places': places['bus']['reserved_limit'],
            'parking': parking
        }
        PlaceSerializer.create(PlaceSerializer(), validated_data=validate_data_bus)

        validate_data_car = {
            'type': car_type,
            'reserved_limit': places['car']['reserved_limit'],
            'remaining_places': places['car']['reserved_limit'],
            'parking': parking
        }
        PlaceSerializer.create(PlaceSerializer(), validated_data=validate_data_car)

        validate_data_motorcycle = {
            'type': motorcycle_type,
            'reserved_limit': places['motorcycle']['reserved_limit'],
            'remaining_places': places['motorcycle']['reserved_limit'],
            'parking': parking
        }
        PlaceSerializer.create(PlaceSerializer(), validated_data=validate_data_motorcycle)

# class ListParkingSerializer(serializers.ModelSerializer):
#     address = AddressSerializer()
#     price = PriceSerializer()
#
#     class Meta:
#         model = Parking
#         fields = "__all__"
#         read_only_fields = (
#             'address',
#             'price',
#         )
