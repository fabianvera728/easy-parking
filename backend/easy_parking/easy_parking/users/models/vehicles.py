from django.db import models
from easy_parking.users.models.users import User
from easy_parking.reservations.models.types import Type as TypeVehicle

class Vehicle(models.Model):
    """Model definition for Vehicle."""

    # TODO: Define fields here
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    license_plate = models.TextField(max_length=50)
    type = models.ForeignKey(TypeVehicle)
    brand_vehicle = models.TextField(max_length=50)

    class Meta:
        """Meta definition for Vehicle."""

        verbose_name = 'Vehicle'
        verbose_name_plural = 'Vehicles'

    def __str__(self):
        """Unicode representation of Vehicle."""
        pass
