from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import authentication, permissions
from easy_parking.users.models.profiles import Profile
from easy_parking.users.serializers.profile import ProfileSerializer
from rest_framework.parsers import JSONParser

class ListUsers(APIView):
    
    def get(self, request, format=None):
        users =  Profile.objects.all()
        serializer = ProfileSerializer(users, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, format=None):
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data}, status=200) 
        return Response(serializer.errors, status=400)