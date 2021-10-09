# Django
from django.db import models


class Service(models.Model):
    """Model definition for Service."""

    name = models.TextField(max_length=50)
    verbose_name = models.TextField(max_length=70, blank=True)
    description = models.TextField(max_length=500, blank=True)

    class Meta:
        """Meta definition for Service."""

        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    def __str__(self):
        return f'Service {self.name}'
