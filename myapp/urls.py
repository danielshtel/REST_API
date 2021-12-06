from django.conf.urls import url
from django.urls import path, re_path
from .views import *
''

urlpatterns = [
    path('drivers/driver', DriverViewSet.as_view(), name='all_drivers'),
    re_path(r'^drivers/driver/', DriverViewSet.as_view(), name='driver_filter'),
]
