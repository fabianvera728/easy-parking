from django.db.models import fields
from rest_framework import serializers
from easy_parking.reservations.models.types import Type as TypeVehicle

class TypeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = TypeVehicle
        fields = "__all__"
        
    def create(self, validated_data):
        """
        Overriding the default create method of the Model serializer.
        :param validated_data: data containing all the details of student
        :return: returns a successfully created student record
        """
        type_vehicle, created = TypeVehicle.objects.update_or_create(
                            name=validated_data.pop('name'), 
                            description=validated_data.pop('description'), 
                            verbose_name=validated_data.pop('verbose_name')
                            )
        return type_vehicle