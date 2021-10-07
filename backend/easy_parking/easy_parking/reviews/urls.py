# Django
from django.urls import path, include

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from easy_parking.reviews.views.comments import Comments
from easy_parking.reviews.views.reviews import Reviews

router = DefaultRouter()
router.register(r'comments', Comments, basename='comment')
router.register(r'reviews', Reviews, basename='review')

urlpatterns = [
    path('', include(router.urls))
]
