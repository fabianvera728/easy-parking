# Django restframework
from rest_framework import serializers

# Models
from easy_parking.reservations.models.types import Type as TypeVehicle


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeVehicle
        fields = "__all__"

    def create(self, validated_data):
        type_vehicle, created = TypeVehicle.objects.update_or_create(**validated_data)
        return type_vehicle
