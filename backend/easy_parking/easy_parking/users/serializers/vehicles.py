# Django est framework
from rest_framework import serializers

# Models
from easy_parking.users.models.vehicles import Vehicle


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = "__all__"

    def create(self, validated_data):
        vehicle, created = Vehicle.objects.update_or_create(**validated_data)
        return vehicle
