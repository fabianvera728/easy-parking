from django.db import models
from django.contrib.auth.models import AbstractUser
from easy_parking.utils.base_model import BaseModel


class User(BaseModel, AbstractUser):
    pass

