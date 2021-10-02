from django.db import models
from easy_parking.parking_lots.models.parking_lots import Parking

class Image(models.Model):
    """Model definition for Image."""

    # TODO: Define fields here
    path = models.ImageField()
    verbose_name = models.TextField()
    parking = models.ForeignKey(Parking, on_delete=models.CASCADE)

    class Meta:
        """Meta definition for Image."""

        verbose_name = 'Image'
        verbose_name_plural = 'Images'

    def __str__(self):
        """Unicode representation of Image."""
        pass
