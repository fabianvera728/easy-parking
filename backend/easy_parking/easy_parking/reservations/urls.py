from django.urls import path
from easy_parking.reservations.views.reservations import ListReservations
from easy_parking.reservations.views.places import ListPlaces
from easy_parking.reservations.views.types import ListTypes

urlpatterns = [
    path('types/', ListTypes.as_view(), name="view types"),
    path('places/', ListPlaces.as_view(), name="view places"),
    path('reservations/', ListReservations.as_view(), name="view reservations")
]