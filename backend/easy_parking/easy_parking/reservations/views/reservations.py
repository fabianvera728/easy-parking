from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import authentication, permissions
from easy_parking.reservations.models.reservations import Reservation
from easy_parking.reservations.serializers.reservations import ReservationSerializer
from rest_framework.parsers import JSONParser

class ListReservations(APIView):
    
    def get(self, request, format=None):
        reservations =  Reservation.objects.all()
        serializer = ReservationSerializer(reservations, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, format=None):
        print(request.data)
        serializer = ReservationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data}, status=200) 
        return Response(serializer.errors, status=400)