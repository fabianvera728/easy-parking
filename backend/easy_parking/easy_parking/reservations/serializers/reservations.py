from django.db.models import fields
from rest_framework import serializers
from easy_parking.reservations.models.reservations import Reservation

class ReservationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Reservation
        fields = "__all__"
    
    """ def create(self, validated_data):
        
        reservation, created = Reservation.objects.update_or_create(vehicle=validated_data.pop('vehicle'), 
                            parking=validated_data.pop('parking'), 
                            start_timestamp=validated_data.pop('start_timestamp'),
                            final_timestamp=validated_data.pop('final_timestamp'),
                            is_reserved=validated_data.pop('is_reserved'),
                            is_active=validated_data.pop('is_active'),
                            net_cost=validated_data.pop('net_cost'),
                            is_paid=validated_data.pop('is_paid')
                            )
        return reservation """
    def create(self, validated_data):
        """
        Overriding the default create method of the Model serializer.
        :param validated_data: data containing all the details of student
        :return: returns a successfully created student record
        """
        reservation, created = Reservation.objects.update_or_create(vehicle=validated_data.pop('vehicle'), 
                            parking=validated_data.pop('parking'), 
                            is_reserved=validated_data.pop('is_reserved'),
                            is_active=validated_data.pop('is_active'),
                            net_cost=validated_data.pop('net_cost'),
                            is_paid=validated_data.pop('is_paid')
                            )
        return reservation
    