from django.conf.urls import url
from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('drivers/driver/<int:driver_id>/', DriverCRUDSet.as_view(), name='get_driver_pk'),
    re_path(r'^drivers/driver/', DriverViewSet.as_view(), name='driver_filter'),

]
