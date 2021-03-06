# Django
from django.db import models

# Models
from easy_parking.users.models.users import User
from easy_parking.utils.base_model import BaseModel


class Profile(BaseModel):
    phone_number = models.CharField(max_length=20)
    reputation = models.FloatField(default=5.0)
    picture = models.ImageField('profile picture',
                                upload_to='users/pictures/',
                                blank=True,
                                null=True)
    biography = models.TextField(max_length=500, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return str(self.user)
