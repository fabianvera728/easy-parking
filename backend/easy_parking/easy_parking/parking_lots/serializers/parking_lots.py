from django.db.models import fields
from easy_parking.parking_lots.models.prices import Price
from easy_parking.parking_lots.serializers.prices import PriceSerializer
from easy_parking.parking_lots.models.addresses import Address
from rest_framework import serializers
from easy_parking.parking_lots.models.parking_lots import Parking
from easy_parking.parking_lots.serializers.addresses import AddressSerializer

class ParkingSerializer(serializers.ModelSerializer):
    address = AddressSerializer()
    price = PriceSerializer()
    class Meta:
        model = Parking
        fields = "__all__"
        
    def create(self, validated_data):
        """
        Overriding the default create method of the Model serializer.
        :param validated_data: data containing all the details of student
        :return: returns a successfully created student record
        """
        address_data = validated_data.pop("address")
        address = Address.objects.create(**address_data) 
        price_data = validated_data.pop("price")
        price = Price.objects.create(**price_data)
        
        parking, created = Parking.objects.update_or_create(
                            owner=validated_data.pop('owner'), 
                            slug_name=validated_data.pop('slug_name'), 
                            description=validated_data.pop('description'),
                            phone_number=validated_data.pop('phone_number'),
                            price=price,
                            address=address,
                            limit_image=validated_data.pop('limit_image')
                            )
        return parking