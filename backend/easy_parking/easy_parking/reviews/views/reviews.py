# Django restframework
from rest_framework import mixins, viewsets

# Models
from easy_parking.reviews.models.reviews import Review

# Serializers
from easy_parking.reviews.serializers.reviews import ReviewSerializer


class Reviews(mixins.CreateModelMixin,
               mixins.RetrieveModelMixin,
               mixins.UpdateModelMixin,
               mixins.ListModelMixin,
               viewsets.GenericViewSet):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()
