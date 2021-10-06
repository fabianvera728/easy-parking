from easy_parking.parking_lots.serializers.addresses import AddressSerializer
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import authentication, permissions
from easy_parking.parking_lots.models.parking_lots import Parking
from easy_parking.parking_lots.serializers.parking_lots import ParkingSerializer
from rest_framework.parsers import JSONParser
from easy_parking.parking_lots.serializers.prices import PriceSerializer

class ListParkings(APIView):
    
    def get(self, request, format=None):
        users =  Parking.objects.all()
        serializer = ParkingSerializer(users, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, format=None):
        print(request.data['address'])
        """ address = AddressSerializer(data=request.data['address'])
        if address.is_valid():
            address.save()  
        price = PriceSerializer(data=request.data['price'])
        if price.is_valid():
            price.save()
            
        request.data['address'] = address.data['id']
        request.data['price'] = price.data['id'] """
        
        serializer = ParkingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data}, status=200) 
        return Response(serializer.errors, status=400)