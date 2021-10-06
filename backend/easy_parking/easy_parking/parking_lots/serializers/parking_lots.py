from django.db.models import fields
from easy_parking.parking_lots.models.addresses import Address
from rest_framework import serializers
from easy_parking.parking_lots.models.parking_lots import Parking
from easy_parking.parking_lots.serializers.addresses import AddressSerializer

class ParkingSerializer(serializers.ModelSerializer):
    # address = AddressSerializer()
    """ class Meta:
        model = Parking
        fields = "__all__" """
    class Meta:
        model = Parking
        fields = ["__all__", "address"]    
        
        """ owner = models.ForeignKey(Profile, on_delete=CASCADE)
    slug_name = models.SlugField(max_length=50)
    description = models.TextField(max_length=255)
    phone_number = models.CharField(max_length=20)
    price = models.ForeignKey(Price, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, null=True, on_delete=models.CASCADE)
    limit_image = models.IntegerField() """
        
    def create(self, validated_data):
        """
        Overriding the default create method of the Model serializer.
        :param validated_data: data containing all the details of student
        :return: returns a successfully created student record
        """
        #   address_data = validated_data.pop("address")
        #print(address_data)
        #print(validated_data)
        #address = Address.objects.create(**address_data) 
        """ address = AddressSerializer.create(AddressSerializer(), validated_data=address_data)
        print(address.pk) """
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