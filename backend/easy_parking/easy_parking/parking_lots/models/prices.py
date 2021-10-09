# Django
from django.db import models


class Price(models.Model):
    """Model definition for Price."""

    morning = models.FloatField()
    evening = models.FloatField()
    night = models.FloatField()
    weekend = models.FloatField()

    class Meta:
        """Meta definition for Price."""

        verbose_name = 'Price'
        verbose_name_plural = 'Prices'

    def __str__(self):
        return f'Prices: [{self.morning}, ' \
               f'{self.evening}, {self.night},' \
               f' {self.weekend}, ]'
