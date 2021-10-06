from django.db import models
from easy_parking.users.models.vehicles import Vehicle
from easy_parking.parking_lots.models.parking_lots import Parking

class Reservation(models.Model):
    """Model definition for Reservation."""

    # TODO: Define fields here
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    parking = models.ForeignKey(Parking, on_delete=models.CASCADE)
    start_timestamp = models.DateTimeField(auto_now_add=True)
    final_timestamp = models.DateTimeField(auto_now_add=True)
    is_reserved = models.BooleanField()
    is_active = models.BooleanField()
    net_cost = models.FloatField()
    is_paid = models.FloatField()
    
    class Meta:
        """Meta definition for Reservation."""

        verbose_name = 'Reservation'
        verbose_name_plural = 'Reservations'

    def __str__(self):
        """Unicode representation of Reservation."""
        pass
