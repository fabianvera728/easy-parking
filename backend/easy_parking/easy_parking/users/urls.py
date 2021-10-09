# Django
from django.urls import path, include

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from easy_parking.users.views.vehicles import Vehicles
from easy_parking.users.views.users import Users

router = DefaultRouter()
router.register(r'vehicles', Vehicles, basename='vehicle')
router.register(r'users', Users, basename='user')

urlpatterns = [
    path('', include(router.urls))
]
