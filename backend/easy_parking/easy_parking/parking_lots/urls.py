from django.urls import path
from easy_parking.parking_lots.views.addresses import ListAddresses
from easy_parking.parking_lots.views.prices import ListPrices
from easy_parking.parking_lots.views.parking_lots import ListParkings

urlpatterns = [
    path('parkings/', ListParkings.as_view(), name="view parkings"),
    path('prices/', ListPrices.as_view(), name="view prices"),
    path('addresses/', ListAddresses.as_view(), name="view addresses"),
]