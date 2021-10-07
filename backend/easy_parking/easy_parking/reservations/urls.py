# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from .views.reservations import Reservations
from .views.places import Places
from .views.types import Types

# urlpatterns = [
#     path('reservations/', Reservations.as_view(), name="reservations"),
#     path('places/', Places.as_view(), name="places"),
#     path('reservations/types/', Types.as_view(), name="types")
# ]

router = DefaultRouter()
router.register(r'reservations', Reservations, basename='reservation')
router.register(r'places', Places, basename='place')
router.register(r'types', Types, basename='type')

urlpatterns = [
    path('', include(router.urls))
]
