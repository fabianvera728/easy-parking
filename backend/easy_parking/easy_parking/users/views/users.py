# Django Restframework
from rest_framework import mixins,status,  viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

# Models
from easy_parking.users.models.profiles import Profile
from easy_parking.reservations.models.reservations import Reservation
from easy_parking.users.models.vehicles import Vehicle
from easy_parking.parking_lots.models.parking_lots import Parking

# Serializers
from easy_parking.users.serializers.profile import ProfileSerializer
from easy_parking.reservations.serializers.reservations import ReservationSerializer
from easy_parking.users.serializers.vehicles import VehicleSerializer
from easy_parking.parking_lots.serializers.parking_lots import ParkingSerializer
from easy_parking.users.serializers.users import UserLoginSerializer


class Users(mixins.CreateModelMixin,
            mixins.RetrieveModelMixin,
            mixins.UpdateModelMixin,
            mixins.ListModelMixin,
            viewsets.GenericViewSet):
    lookup_field = 'user__username'
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()

    @action(detail=False, methods=['post'])
    def login(self, request):
        """User sign in."""
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, token = serializer.save()
        data = {
            'user': ProfileSerializer(Profile.objects.get(user=user)).data,
            'access_token': token
        }
        return Response(data, status=status.HTTP_201_CREATED)

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
    
    @action(detail=True, methods=['get'])
    def parkings(self, request, *args, **kwargs):
        parkings = Parking.objects.filter(owner=self.get_object())
        serializer = ParkingSerializer(parkings, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def parkings(self, request, *args, **kwargs):
        parkings = Parking.objects.filter(owner=self.get_object())
        serializer = ParkingSerializer(parkings, many=True)
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
