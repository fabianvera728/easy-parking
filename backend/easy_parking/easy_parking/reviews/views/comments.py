# Django restframework
from rest_framework import mixins, viewsets

# Models
from easy_parking.reviews.models.comments import Comment

# Serializers
from easy_parking.reviews.serializers.comments import CommentSerializer


class Comments(mixins.CreateModelMixin,
               mixins.RetrieveModelMixin,
               mixins.UpdateModelMixin,
               mixins.ListModelMixin,
               viewsets.GenericViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
