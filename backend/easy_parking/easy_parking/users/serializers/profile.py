# Django restframework
from rest_framework import serializers

# Models
from easy_parking.users.models.profiles import Profile

# Serializers
from easy_parking.users.serializers.users import UserSerializer


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)

    class Meta:
        model = Profile
        fields = "__all__"

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        validated_data.user = user
        profile, created = Profile.objects.update_or_create(**validated_data)
        return profile
