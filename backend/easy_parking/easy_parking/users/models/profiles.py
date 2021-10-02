from django.db import models
from easy_parking.users.models.users import User
from easy_parking.utils.base_model import BaseModel

class Profile(BaseModel):
    phone_number = models.IntegerField()
    reputation = models.FloatField(default=0)
    picture = models.TextField()
    biography = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)