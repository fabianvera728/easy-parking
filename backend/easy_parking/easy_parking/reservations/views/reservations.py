# Django restframework
from rest_framework import mixins, viewsets

# Models
from easy_parking.reservations.models.reservations import Reservation
from easy_parking.reservations.serializers.reservations import ReservationSerializer


class Reservations(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    serializer_class = ReservationSerializer
    queryset = Reservation.objects.all()

    # def get(self, request, format=None):
    #     reservations = Reservation.objects.all()
    #     serializer = ReservationSerializer(reservations, many=True)
    #     return Response(serializer.data)
    #
    # def post(self, request, *args, format=None):
    #     print(request.data)
    #     serializer = ReservationSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response({'data': serializer.data}, status=200)
    #     return Response(serializer.errors, status=400)
