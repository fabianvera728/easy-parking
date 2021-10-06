from django.db.models import fields
from rest_framework import serializers
from easy_parking.users.models.users import User
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"