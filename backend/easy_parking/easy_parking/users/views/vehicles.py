from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from easy_parking.users.models.vehicles import Vehicle
from easy_parking.users.serializers.vehicles import VehicleSerializer
from rest_framework.parsers import JSONParser

class ListVehicles(APIView):
    
    def get(self, request, format=None):
        vehicles =  Vehicle.objects.all()
        serializer = VehicleSerializer(vehicles, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, format=None):
        serializer = VehicleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data}, status=200) 
        return Response(serializer.errors, status=400)