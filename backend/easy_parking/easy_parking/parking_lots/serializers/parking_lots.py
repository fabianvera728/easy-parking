from rest_framework import serializers

from easy_parking.parking_lots.models.addresses import Address
from easy_parking.parking_lots.models.parking_lots import Parking
from easy_parking.parking_lots.models.prices import Price
from easy_parking.parking_lots.serializers.addresses import AddressSerializer
from easy_parking.parking_lots.serializers.prices import PriceSerializer


class ParkingSerializer(serializers.ModelSerializer):
    address = AddressSerializer()
    price = PriceSerializer()

    class Meta:
        model = Parking
        fields = "__all__"

    def create(self, validated_data):
        address_data = validated_data["address"]
        price_data = validated_data["price"]

        address = Address.objects.create(**address_data)
        price = Price.objects.create(**price_data)

        validated_data["address"] = address
        validated_data["price"] = price

        parking, created = Parking.objects.update_or_create(**validated_data)
        return parking
