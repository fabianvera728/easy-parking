from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import authentication, permissions
from easy_parking.reservations.models.types import Type as TypeVehicle
from easy_parking.reservations.serializers.types import TypeSerializer
from rest_framework.parsers import JSONParser

class ListTypes(APIView):
    
    def get(self, request, format=None):
        types =  TypeVehicle.objects.all()
        serializer = TypeSerializer(types, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, format=None):
        serializer = TypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data}, status=200) 
        return Response(serializer.errors, status=400)