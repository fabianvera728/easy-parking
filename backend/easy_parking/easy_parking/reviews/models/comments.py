from django.db import models
from easy_parking.reviews.models.reviews import Review

class Comment(models.Model):
    """Model definition for Comments."""

    # TODO: Define fields here
    comments = models.BooleanField(default=False)
    response = models.FloatField(default=0)
    interaction = models.ForeignKey(Review, on_delete=models.CASCADE)

    class Meta:
        """Meta definition for Comments."""

        verbose_name = 'Comments'
        verbose_name_plural = 'Commentss'

    def __str__(self):
        """Unicode representation of Comments."""
        pass
