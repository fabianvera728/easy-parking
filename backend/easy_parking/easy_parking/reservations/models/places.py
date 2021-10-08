# Django
from django.db import models

# Django restframework
from easy_parking.parking_lots.models.parking_lots import Parking
from easy_parking.reservations.models.types import Type as TypeVehicle


class Place(models.Model):
    """Model definition for Place."""

    type = models.ForeignKey(TypeVehicle, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    parking = models.ForeignKey(Parking, on_delete=models.CASCADE)
    description = models.TextField(max_length=500, blank=True)

    used_places = models.PositiveIntegerField(default=0)
    remaining_places = models.PositiveIntegerField(default=0)
    reserved_limit = models.PositiveIntegerField(default=0)

    class Meta:
        """Meta definition for Place."""
        verbose_name = 'Place'
        verbose_name_plural = 'Places'

    def __str__(self):
        return f'{self.type} on {self.parking}'
