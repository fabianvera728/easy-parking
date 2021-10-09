# Django restframework
from rest_framework import serializers

# Models
from easy_parking.users.models.vehicles import Vehicle
from easy_parking.reservations.models.reservations import Reservation
from easy_parking.parking_lots.models.parking_lots import Parking
from easy_parking.reservations.models.places import Place


class ReservationSerializer(serializers.ModelSerializer):
    parking = serializers.CharField(max_length=200)
    vehicle = serializers.CharField(max_length=200)

    class Meta:
        model = Reservation
        fields = "__all__"
        read_only_fields = (
            'parking',
            'vehicle',
        )

    def create(self, validated_data):
        validated_data.pop('parking')
        validated_data.pop('vehicle')
        parking = self.context['parking']
        vehicle = self.context['vehicle']
        if self.not_there_are_places():
            raise serializers.ValidationError('Not places available.')
        self.increase_used_places()
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
        self.context['parking'] = parking
        return data

    def validate_vehicle(self, data):
        try:
            vehicle = Vehicle.objects.get(
                license_plate=data
            )
        except Vehicle.DoesNotExist:
            raise serializers.ValidationError('Invalid license plate of vehicle.')
        self.context['vehicle'] = vehicle
        return data

    def not_there_are_places(self):
        self.context['place'] = Place.objects.get(parking=self.context['parking'],
                                                  type=self.context['vehicle'].type)
        return self.context['place'].remaining_places == 0

    def increase_used_places(self):
        self.context['place'].used_places = self.context['place'].used_places + 1
        self.context['place'].remaining_places = self.context['place'].reserved_limit - self.context[
            'place'].used_places
        self.context['place'].save()

# class ListReservationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Reservation
#         fields = "__all__"
