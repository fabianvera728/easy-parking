# Django
from django.db import models

# Models
from easy_parking.parking_lots.models.parking_lots import Parking


class Image(models.Model):
    """Model definition for Image."""

    path = models.ImageField("Parking's image",
                             upload_to='parking/gallery/',
                             blank=True,
                             null=True)
    verbose_name = models.TextField(blank=True)
    parking = models.ForeignKey(Parking, on_delete=models.CASCADE)

    class Meta:
        """Meta definition for Image."""

        verbose_name = 'Image'
        verbose_name_plural = 'Images'

    def __str__(self):
        return f"Image of {self.parking}' gallery"
