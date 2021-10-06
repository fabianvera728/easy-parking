from django.db.models import fields
from rest_framework import serializers
from easy_parking.users.models.profiles import Profile
from easy_parking.users.serializers.users import UserSerializer

class ProfileSerializer(serializers.ModelSerializer):

    user = UserSerializer(required=True)
    
    class Meta:
        model = Profile
        fields = ("phone_number", "reputation", "picture", "biography", "user")
        
    def create(self, validated_data):
        """
        Overriding the default create method of the Model serializer.
        :param validated_data: data containing all the details of student
        :return: returns a successfully created student record
        """
        user_data = validated_data.pop('user')
        user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        profile, created = Profile.objects.update_or_create(user=user,
                            phone_number=validated_data.pop('phone_number'), 
                            reputation=validated_data.pop('reputation'), 
                            picture=validated_data.pop('picture'),
                            biography=validated_data.pop('biography'))
        return profile