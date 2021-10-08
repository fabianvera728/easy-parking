# Django
from django.contrib.auth import password_validation, authenticate
from django.core.validators import RegexValidator

# Django restframework
from rest_framework import serializers
from rest_framework.authtoken.models import Token

# Models
from easy_parking.users.models.users import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class UserLoginSerializer(serializers.Serializer):
    """User login serializer.
    Handle the login request data.
    """

    username = serializers.CharField(min_length=3, max_length=30)
    password = serializers.CharField(min_length=8, max_length=64)

    def validate(self, data):
        """Check credentials."""
        user = User.objects.get(username=data['username'], password=data['password'])
        if not user:
            raise serializers.ValidationError('Invalid credentials')
        self.context['user'] = user
        return data

    def create(self, data):
        """Generate or retrieve new token."""
        return self.context['user'], 'wilmer'
