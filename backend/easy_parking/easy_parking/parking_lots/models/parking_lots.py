from django.db import models
from easy_parking.users.models.users import User

class Parking(models.Model):
    """Model definition for Parking."""

    # TODO: Define fields here
    owner = models.ForeignKey(User)
    slug_name = models.SlugField()
    description = models.TextField()
    phone_number = models.IntegerField()
    price = models.FloatField()
    limit_image = models.TextField()

    class Meta:
        """Meta definition for Parking."""

        verbose_name = 'Parking'
        verbose_name_plural = 'Parkings'

    def __str__(self):
        """Unicode representation of Parking."""
        pass
