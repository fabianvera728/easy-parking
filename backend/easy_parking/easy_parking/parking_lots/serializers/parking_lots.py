from django.db.models import fields
from rest_framework import serializers
from easy_parking.parking_lots.models.parking_lots import Parking

class ParkingSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Parking
        fields = "__all__"
        
    def create(self, validated_data):
        """
        Overriding the default create method of the Model serializer.
        :param validated_data: data containing all the details of student
        :return: returns a successfully created student record
        """
        parking, created = Parking.objects.update_or_create(
                            owner=validated_data.pop('owner'), 
                            slug_name=validated_data.pop('slug_name'), 
                            description=validated_data.pop('description'),
                            phone_number=validated_data.pop('phone_number'),
                            price=validated_data.pop('price'),
                            address=validated_data.pop('address'),
                            limit_image=validated_data.pop('limit_image')
                            )
        return parking