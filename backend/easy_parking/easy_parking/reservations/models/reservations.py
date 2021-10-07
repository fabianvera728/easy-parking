# Django
from django.db import models

# Models
from easy_parking.users.models.vehicles import Vehicle
from easy_parking.parking_lots.models.parking_lots import Parking


class Reservation(models.Model):
    """Model definition for Reservation."""

    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    parking = models.ForeignKey(Parking, on_delete=models.CASCADE)
    start_timestamp = models.DateTimeField(auto_now_add=True)
    final_timestamp = models.DateTimeField(auto_now_add=True)
    is_reserved = models.BooleanField(default=True)
    is_active = models.BooleanField(default=False)
    net_cost = models.FloatField(default=0)
    is_paid = models.FloatField(default=False)

    class Meta:
        verbose_name = 'Reservation'
        verbose_name_plural = 'Reservations'

    def __str__(self):
        return f'{self.vehicle} in {self.parking}'
