from django.db.models import fields
from rest_framework import serializers
from easy_parking.parking_lots.models.addresses import Address

class AddressSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Address
        fields = "__all__"
    
    def create(self, validated_data):
        """
        Overriding the default create method of the Model serializer.
        :param validated_data: data containing all the details of student
        :return: returns a successfully created student record
        """
        address, created = Address.objects.update_or_create(
                            country=validated_data.pop('country'), 
                            state=validated_data.pop('state'), 
                            city=validated_data.pop('city'),
                            street=validated_data.pop('street'),
                            number_street=validated_data.pop('number_street'),
                            neighbothood=validated_data.pop('neighbothood'),
                            description=validated_data.pop('description'),
                            )
        return address
    