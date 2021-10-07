# Django restframework
from rest_framework import serializers

# Models
from easy_parking.reviews.models.comments import Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"

    def create(self, validated_data):
        review, created = Review.objects.update_or_create(**validated_data)
        return review
