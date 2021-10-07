# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from .views.parking_lots import Parkings
from .views.prices import Prices
from .views.addresses import Addresses

# urlpatterns = [
#     path('reservations/', Reservations.as_view(), name="reservations"),
#     path('places/', Places.as_view(), name="places"),
#     path('reservations/types/', Types.as_view(), name="types")
# ]

router = DefaultRouter()
router.register(r'parkings', Parkings, basename='parking')
router.register(r'prices', Prices, basename='price')
router.register(r'addresses', Addresses, basename='address')

urlpatterns = [
    path('', include(router.urls))
]

# urlpatterns = [
#     path('parkings/', Parking, name="view parkings"),
#     path('prices/', ListPrices.as_view(), name="view prices"),
#     path('addresses/', ListAddresses.as_view(), name="view addresses"),
# ]