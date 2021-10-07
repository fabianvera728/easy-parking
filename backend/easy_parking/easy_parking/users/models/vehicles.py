# Django
from django.db import models

# Models
from easy_parking.users.models.profiles import Profile
from easy_parking.reservations.models.types import Type as TypeVehicle
from easy_parking.utils.base_model import BaseModel


class Vehicle(BaseModel):
    """Model definition for Vehicle."""

    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
    type = models.ForeignKey(TypeVehicle, on_delete=models.CASCADE)
    license_plate = models.TextField(max_length=50, unique=True)
    brand_vehicle = models.TextField(max_length=50)
    description = models.TextField(max_length=500, blank=True)

    class Meta:
        """Meta definition for Vehicle."""

        verbose_name = 'Vehicle'
        verbose_name_plural = 'Vehicles'

    def __str__(self):
        """Unicode representation of Vehicle."""
        return f'{self.license_plate}'
