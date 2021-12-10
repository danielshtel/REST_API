from rest_framework import routers

from .views import *

router = routers.SimpleRouter()
router.register(r'drivers/driver', DriverViewSet)
router.register(r'vehicles/vehicle', VehicleViewSet)
urlpatterns = []

urlpatterns += router.urls
