# Django Restframework
from rest_framework import mixins, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

# Models
from easy_parking.users.models.profiles import Profile
from easy_parking.reservations.models.reservations import Reservation
from easy_parking.users.models.vehicles import Vehicle

# Serializers
from easy_parking.users.serializers.profile import ProfileSerializer
from easy_parking.reservations.serializers.reservations import ReservationSerializer
from easy_parking.users.serializers.vehicles import VehicleSerializer

class Users(mixins.CreateModelMixin,
            mixins.RetrieveModelMixin,
            mixins.UpdateModelMixin,
            mixins.ListModelMixin,
            viewsets.GenericViewSet):
    lookup_field = 'user__username'
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()

    @action(detail=True, methods=['get'])
    def reservations(self, request, *args, **kwargs):
        reservations = Reservation.objects.filter(vehicle__owner__user=self.get_object())
        serializer = ReservationSerializer(reservations, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def vehicles(self, request, *args, **kwargs):
        vehicles = Vehicle.objects.filter(owner=self.get_object())
        serializer = VehicleSerializer(vehicles, many=True)
        return Response(serializer.data)

# class ListUsers(APIView):
#
#     def get(self, request, format=None):
#         users = Profile.objects.all()
#         serializer = ProfileSerializer(users, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, *args, format=None):
#         serializer = ProfileSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'data': serializer.data}, status=200)
#         return Response(serializer.errors, status=400)
