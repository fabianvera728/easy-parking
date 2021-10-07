# Django
from django.db import models

# Models
from easy_parking.parking_lots.models.parking_lots import Parking
from easy_parking.users.models.users import User


class Review(models.Model):
    like = models.BooleanField(default=False)
    valoration = models.FloatField(default=5.0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    parking = models.ForeignKey(Parking, on_delete=models.CASCADE)
