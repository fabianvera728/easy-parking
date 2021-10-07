# Django Restframework
from rest_framework import mixins, viewsets

# Models
from easy_parking.users.models.profiles import Profile

# Serializers
from easy_parking.users.serializers.profile import ProfileSerializer


class Users(mixins.CreateModelMixin,
            mixins.RetrieveModelMixin,
            mixins.UpdateModelMixin,
            mixins.ListModelMixin,
            viewsets.GenericViewSet):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()


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
