from django.db.models import fields
from rest_framework import serializers
from easy_parking.parking_lots.models.prices import Price

class PriceSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Price
        fields = "__all__"
        
    def create(self, validated_data):
        """
        Overriding the default create method of the Model serializer.
        :param validated_data: data containing all the details of student
        :return: returns a successfully created student record
        """
        price, created = Price.objects.update_or_create(
                            morning=validated_data.pop('morning'), 
                            evening=validated_data.pop('evening'), 
                            night=validated_data.pop('night'),
                            weekend=validated_data.pop('weekend')
                            )
        return price
    