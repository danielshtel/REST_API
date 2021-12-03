import datetime

from django.core import serializers
from django.shortcuts import render
from django.views.generic import ListView
from .models import Driver, Vehicle
import json
from django.http import JsonResponse, HttpResponse


class DriverView(ListView):
    pass


# TODO all drivers list


def driver_gte_date(request):
    data = json.loads(request.body)
    print(data)
    driver = Driver.objects.filter(created_at__gte=datetime.date(year=data['year'],
                                                                 month=data['month'],
                                                                 day=data['day']))
    serialized = json.loads(serializers.serialize('json', driver, fields=('first_name', 'last_name',
                                                                          'created_at', 'updated_at',)))

    return JsonResponse(serialized, safe=False)
