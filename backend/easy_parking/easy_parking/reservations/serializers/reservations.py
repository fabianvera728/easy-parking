# Django restframework
from rest_framework import serializers

# Models
from easy_parking.users.models.vehicles import Vehicle
from easy_parking.reservations.models.reservations import Reservation
from easy_parking.parking_lots.models.parking_lots import Parking

# Serializers
from easy_parking.parking_lots.serializers.parking_lots import ParkingSerializer
from easy_parking.users.serializers.vehicles import VehicleSerializer


class ReservationSerializer(serializers.ModelSerializer):
    vehicle = VehicleSerializer()
    parking = ParkingSerializer()

    class Meta:
        model = Reservation
        fields = "__all__"

    def create(self, validated_data):
        parking = Parking.objects.get(slug_name=validated_data.pop('parking'))
        vehicle = Vehicle.objects.get(license_plate=validated_data.pop('vehicle'))
        validated_data.parking = parking
        validated_data.vehicle = vehicle
        # reservation, created = Reservation.objects.update_or_create(vehicle=vehicle,
        #                                                             parking=parking,
        #                                                             is_reserved=validated_data.pop('is_reserved'),
        #                                                             is_active=validated_data.pop('is_active'),
        #                                                             net_cost=validated_data.pop('net_cost'),
        #                                                             is_paid=validated_data.pop('is_paid')
        #                                                             )
        reservation, created = Reservation.objects.update_or_create(**validated_data)
        return reservation
