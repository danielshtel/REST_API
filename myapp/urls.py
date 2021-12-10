from django.urls import path
from rest_framework import routers

from .views import *

router = routers.SimpleRouter()
router.register(r'drivers/driver', DriverViewSet)
router.register(r'vehicles/vehicle', VehicleViewSet)
urlpatterns = [path('vehicles/set_driver/<pk>/', VehicleDriverViewSet.as_view({'post': 'set_driver'})), ]

urlpatterns += router.urls
