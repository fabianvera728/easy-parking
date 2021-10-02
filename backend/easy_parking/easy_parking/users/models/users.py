from django.contrib.auth import models as models_contrib
from easy_parking.utils.base_model import BaseModel


class User(BaseModel, models_contrib.User):
    pass