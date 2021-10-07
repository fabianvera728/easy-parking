# Django
from django.db import models


class Address(models.Model):
    """Model definition for Address."""

    country = models.TextField(max_length=50)
    state = models.TextField(max_length=50)
    city = models.TextField(max_length=50)
    street = models.TextField(max_length=50)
    number_street = models.IntegerField()
    neighborhood = models.TextField(max_length=50, blank=True)
    description = models.TextField(max_length=254, blank=True)

    class Meta:
        """Meta definition for Address."""

        verbose_name = 'Address'
        verbose_name_plural = 'Addresses'

    def __str__(self):
        return f'{self.street}, {self.neighborhood}. {self.city} - {self.country}.'
