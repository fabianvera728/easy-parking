# Django restframework
from rest_framework import mixins, viewsets

# Models
from easy_parking.reservations.models.places import Place

# Serializers
from easy_parking.reservations.serializers.places import PlaceSerializer


class Places(mixins.CreateModelMixin,
             mixins.RetrieveModelMixin,
             mixins.UpdateModelMixin,
             mixins.ListModelMixin,
             viewsets.GenericViewSet):
    serializer_class = PlaceSerializer
    queryset = Place.objects.all()
# class ListPlaces(APIView):
#
#     def get(self, request, format=None):
#         places =  Place.objects.all()
#         serializer = PlaceSerializer(places, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, *args, format=None):
#         serializer = PlaceSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'data': serializer.data}, status=200)
#         return Response(serializer.errors, status=400)
