from django.db import models

class Type(models.Model):
    """Model definition for Type."""

    # TODO: Define fields here
    name = models.TextField(max_length=50)
    description = models.TextField(max_length=254)
    verbose_name = models.TextField(max_length=50)

    class Meta:
        """Meta definition for Type."""

        verbose_name = 'Type'
        verbose_name_plural = 'Types'

    def __str__(self):
        """Unicode representation of Type."""
        pass
