# Django restframework
from rest_framework import serializers

# Models
from easy_parking.users.models.users import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
