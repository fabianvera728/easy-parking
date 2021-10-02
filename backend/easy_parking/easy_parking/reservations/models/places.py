from django.db import models
from easy_parking.parking_lots.models.parking_lots import Parking

class Place(models.Model):
    """Model definition for Place."""

    # TODO: Define fields here
    type = models.TextField(max_length=255)
    status = models.TextField(max_length=50)
    parking = models.ForeignKey(Parking, on_delete=models.CASCADE)
    
    class Meta:
        """Meta definition for Place."""
        verbose_name = 'Place'
        verbose_name_plural = 'Places'

    def __str__(self):
        """Unicode representation of Place."""
        pass
