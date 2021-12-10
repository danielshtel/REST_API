from django.conf.urls import url
from django.urls import path, re_path
from .views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'drivers/driver', DriverViewSet)
router.register(r'vehicles/vehicle', VehicleViewSet)
urlpatterns = []

urlpatterns += router.urls