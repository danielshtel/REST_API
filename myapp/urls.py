from django.conf.urls import url
from django.urls import path

from .views import *

urlpatterns = [
    # path('drivers/driver', DriverView.as_view()),
    path('drivers/driver/day', driver_gte_date)  # TODO url with parameters, driver list url
]
