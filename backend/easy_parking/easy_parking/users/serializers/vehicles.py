from django.db.models import fields
from rest_framework import serializers
from easy_parking.users.models.vehicles import Vehicle
from easy_parking.users.serializers.users import UserSerializer

class VehicleSerializer(serializers.ModelSerializer):
        
    class Meta:
        model = Vehicle
        fields = "__all__"
        
    def create(self, validated_data):
        """
        Overriding the default create method of the Model serializer.
        :param validated_data: data containing all the details of student
        :return: returns a successfully created student record
        """
        vehicle, created = Vehicle.objects.update_or_create(
                            owner=validated_data.pop('owner'), 
                            license_plate=validated_data.pop('license_plate'), 
                            type=validated_data.pop('type'),
                            brand_vehicle=validated_data.pop('brand_vehicle'))
        return vehicle