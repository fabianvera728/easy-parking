# Django restframework
from rest_framework import serializers

# Models
from easy_parking.reviews.models.comments import Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"

    def create(self, validated_data):
        comment, created = Comment.objects.update_or_create(**validated_data)
        return comment
