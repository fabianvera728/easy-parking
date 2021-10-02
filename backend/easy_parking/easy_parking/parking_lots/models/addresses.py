from django.db import models

class Address(models.Model):
    """Model definition for Address."""

    # TODO: Define fields here
    country = models.TextField(max_length=50)
    state = models.TextField(max_length=50)
    city = models.TextField(max_length=50)
    street = models.TextField(max_length=50)
    number_street = models.IntegerField()
    neighbothood = models.TextField(max_length=50)
    description = models.TextField(max_length=254)
    

    class Meta:
        """Meta definition for Address."""

        verbose_name = 'Address'
        verbose_name_plural = 'Addresss'

    def __str__(self):
        """Unicode representation of Address."""
        pass
