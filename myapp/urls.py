from django.conf.urls import url
from django.urls import path, re_path
from .views import *
''

urlpatterns = [
    path('drivers/driver', drivers_list),
    re_path(r'^drivers/driver/(?P<created_at__gte>)', DriverViewSet.as_view(), name='driver_filter')  # TODO url with parameters, driver list url
]
