from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VehicleViewSet, ServiceViewSet, PetrolViewSet, TripViewSet

router = DefaultRouter()
router.register(r'vehicles', VehicleViewSet)
router.register(r'services', ServiceViewSet)
router.register(r'petrol', PetrolViewSet)
router.register(r'trips', TripViewSet)

urlpatterns = [
    path('', include(router.urls)),
]