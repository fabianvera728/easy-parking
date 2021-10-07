# Django
from django.db import models

# Models
from easy_parking.reviews.models.reviews import Review
from easy_parking.utils.base_model import BaseModel


class Comment(BaseModel):
    """Model definition for Comments."""

    comments = models.TextField(max_length=500)
    response = models.TextField(max_length=500)
    interaction = models.ForeignKey(Review, on_delete=models.CASCADE)

    class Meta:
        """Meta definition for Comments."""

        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __str__(self):
        return f'Comment: {self.comments} in {self.interaction}'
