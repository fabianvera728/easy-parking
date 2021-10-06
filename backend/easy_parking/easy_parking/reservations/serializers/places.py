from django.db.models import fields
from rest_framework import serializers
from easy_parking.reservations.models.places import Place 

class PlaceSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Place
        fields = '__all__'
        
    def create(self, validated_data):
        """
        Overriding the default create method of the Model serializer.
        :param validated_data: data containing all the details of student
        :return: returns a successfully created student record
        """
        place, created = Place.objects.update_or_create(type=validated_data.pop('type'),
                            status=validated_data.pop('status'), 
                            parking=validated_data.pop('parking')
                            )
        return place