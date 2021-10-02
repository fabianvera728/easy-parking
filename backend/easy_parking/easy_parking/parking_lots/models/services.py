from django.db import models

class Service(models.Model):
    """Model definition for Service."""

    # TODO: Define fields here
    name = models.TextField(max_length=50)
    verbose_name = models.TextField(max_length=70)
    description = models.TextField(max_length=254)

    class Meta:
        """Meta definition for Service."""

        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    def __str__(self):
        """Unicode representation of Service."""
        pass
