from django.conf.urls import url
from django.urls import path, re_path
from .views import *
''

urlpatterns = [
    re_path(r'^drivers/driver/', DriverViewSet.as_view(), name='driver_filter')  # TODO url with parameters, driver list url
]
