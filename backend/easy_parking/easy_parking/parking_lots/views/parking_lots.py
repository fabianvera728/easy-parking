# Django restframework
from rest_framework import mixins, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

# Models
from easy_parking.parking_lots.models.parking_lots import Parking

# Serializers
from easy_parking.parking_lots.serializers.parking_lots import ParkingSerializer


class Parkings(mixins.CreateModelMixin,
               mixins.RetrieveModelMixin,
               mixins.UpdateModelMixin,
               mixins.ListModelMixin,
               viewsets.GenericViewSet):
    serializer_class = ParkingSerializer
    queryset = Parking.objects.all()

    lookup_field = 'slug_name'

    @action(detail=True, methods=['get'])
    def invitations(self, request, *args, **kwargs):
        return Response({"data": 'Hola'})

# class ListParkings(APIView):
#
#     def get(self, request):
#         users = Parking.objects.all()
#         serializer = ParkingSerializer(users, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, *args):
#         # print(request.data['address'])
#         """ address = AddressSerializer(data=request.data['address'])
#         if address.is_valid():
#             address.save()
#         price = PriceSerializer(data=request.data['price'])
#         if price.is_valid():
#             price.save()
#
#         request.data['address'] = address.data['id']
#         request.data['price'] = price.data['id'] """
#
#         serializer = ParkingSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'data': serializer.data}, status=200)
#         return Response(serializer.errors, status=400)
