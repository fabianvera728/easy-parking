# Django
from django.db import models
from django.db.models.deletion import CASCADE

# Models
from easy_parking.users.models.profiles import Profile
from easy_parking.parking_lots.models.prices import Price
from easy_parking.parking_lots.models.addresses import Address
from easy_parking.utils.base_model import BaseModel


class Parking(BaseModel):
    """Model definition for Parking."""

    owner = models.ForeignKey(Profile, on_delete=CASCADE)
    name = models.TextField(max_length=50)
    slug_name = models.SlugField(max_length=50, unique=True)
    description = models.TextField(max_length=500, blank=True)
    phone_number = models.CharField(max_length=20)
    price = models.ForeignKey(Price, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, null=True, on_delete=models.CASCADE)
    limit_image = models.PositiveIntegerField(default=20)
    reputation = models.FloatField(default=5.0)

    class Meta:
        """Meta definition for Parking."""

        verbose_name = 'Parking'
        verbose_name_plural = 'Parkings'

    def __str__(self):
        return f'{self.slug_name}'
