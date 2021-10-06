from django.urls import path
from easy_parking.users.views.vehicles import ListVehicles
from easy_parking.users.views.users import ListUsers

urlpatterns = [
    path('users/', ListUsers.as_view(), name="view users"),
    path("vehicles/", ListVehicles.as_view(), name="view vehicles")
]