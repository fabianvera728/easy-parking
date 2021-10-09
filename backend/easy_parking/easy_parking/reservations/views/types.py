# Django restframework
from rest_framework import mixins, viewsets

# Models
from easy_parking.reservations.models.types import Type as TypeVehicle

# Serializers
from easy_parking.reservations.serializers.types import TypeSerializer


class Types(mixins.CreateModelMixin,
            mixins.RetrieveModelMixin,
            mixins.UpdateModelMixin,
            mixins.ListModelMixin,
            viewsets.GenericViewSet):
    serializer_class = TypeSerializer
    queryset = TypeVehicle.objects.all()

# class ListTypes(APIView):
#
#     def get(self, request, format=None):
#         types =  TypeVehicle.objects.all()
#         serializer = TypeSerializer(types, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, *args, format=None):
#         serializer = TypeSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'data': serializer.data}, status=200)
#         return Response(serializer.errors, status=400)
