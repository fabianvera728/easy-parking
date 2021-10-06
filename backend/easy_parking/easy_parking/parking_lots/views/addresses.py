from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import authentication, permissions
from easy_parking.parking_lots.models.addresses import Address
from easy_parking.parking_lots.serializers.addresses import AddressSerializer
from rest_framework.parsers import JSONParser

class ListAddresses(APIView):
    
    def get(self, request, format=None):
        users =  Address.objects.all()
        serializer = AddressSerializer(users, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, format=None):
        serializer = AddressSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data}, status=200) 
        return Response(serializer.errors, status=400)