# Django restframework
from rest_framework import serializers

# Models
from easy_parking.reservations.models.places import Place


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = '__all__'

    def create(self, validated_data):
        place, created = Place.objects.update_or_create(**validated_data)
        return place
