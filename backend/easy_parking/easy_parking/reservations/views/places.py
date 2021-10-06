from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import authentication, permissions
from easy_parking.reservations.models.places import Place
from easy_parking.reservations.serializers.places import PlaceSerializer
from rest_framework.parsers import JSONParser

class ListPlaces(APIView):
    
    def get(self, request, format=None):
        places =  Place.objects.all()
        serializer = PlaceSerializer(places, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, format=None):
        serializer = PlaceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data}, status=200) 
        return Response(serializer.errors, status=400)