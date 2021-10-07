# Django restframework
from rest_framework import serializers
from rest_framework.generics import get_object_or_404

# Models
from easy_parking.users.models.vehicles import Vehicle
from easy_parking.reservations.models.reservations import Reservation
from easy_parking.parking_lots.models.parking_lots import Parking


class ReservationSerializer(serializers.ModelSerializer):
    parking = serializers.CharField(max_length=200)
    vehicle = serializers.CharField(max_length=200)

    class Meta:
        model = Reservation
        fields = "__all__"

    def create(self, validated_data):
        validated_data.pop('parking')
        validated_data.pop('vehicle')
        parking = self.context['parking']
        vehicle = self.context['vehicle']
        reservation = Reservation.objects.create(**validated_data,
                                                 vehicle=vehicle,
                                                 parking=parking)
        return reservation

    def validate_parking(self, data):
        try:
            parking = Parking.objects.get(
                slug_name=data
            )
        except Parking.DoesNotExist:
            raise serializers.ValidationError('Invalid parking slug name.')
        self.context['parking'] = parking.pk
        return data

    def validate_vehicle(self, data):
        try:
            vehicle = Vehicle.objects.get(
                license_plate=data
            )
        except Vehicle.DoesNotExist:
            raise serializers.ValidationError('Invalid license plate of vehicle.')
        self.context['vehicle'] = vehicle.pk
        return data


class ListReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = "__all__"
