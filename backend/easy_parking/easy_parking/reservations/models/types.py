# Django
from django.db import models


class Type(models.Model):
    """Model definition for Type."""

    name = models.TextField(max_length=50)
    description = models.TextField(max_length=254)
    verbose_name = models.TextField(max_length=50, blank=True)

    class Meta:
        verbose_name = 'Type'
        verbose_name_plural = 'Types'

    def __str__(self):
        return f'{self.name}'
