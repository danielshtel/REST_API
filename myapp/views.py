from datetime import datetime

from django.core import serializers
from django.shortcuts import render
from django.views.generic import ListView
from rest_framework.views import APIView

from .models import Driver, Vehicle
import json
from django.http import JsonResponse, HttpResponse, HttpResponseNotFound, HttpResponseBadRequest
from rest_framework import viewsets
from .serializer import DriverSerializer


class DriverViewSet(APIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer

    def get(self, request, *args, **kwargs):
        created_at_gte = self.request.query_params.get('created_at__gte')
        created_at_lte = self.request.query_params.get('created_at__lte')
        if created_at_gte is not None:
            try:
                driver = Driver.objects.filter(created_at__gte=datetime.strptime(created_at_gte, '%d-%m-%Y'))
                driver = DriverSerializer(driver, many=True)
                return JsonResponse(driver.data, safe=False)
            except ValueError:
                return HttpResponseBadRequest('Bad request')

        elif created_at_lte is not None:
            try:
                driver = Driver.objects.filter(created_at__lte=datetime.strptime(created_at_lte, '%d-%m-%Y'))
                driver = DriverSerializer(driver, many=True)
                return JsonResponse(driver.data, safe=False)
            except ValueError:
                return HttpResponseBadRequest('Bad request')


def drivers_list(request):
    drivers = Driver.objects.all()
    serialized = json.loads(serializers.serialize('json', drivers, fields=('first_name', 'last_name',
                                                                           'created_at', 'updated_at',)))
    return JsonResponse(serialized, safe=False)

###########################################################################
# def driver_gte_date(request, *args, **kwargs):
#     query = request.GET.get("created_at__gte", "")
#     if query:
#         try:
#             driver = Driver.objects.filter(created_at__gte=datetime.strptime(query, '%d-%m-%Y'))
#             serialized = json.loads(serializers.serialize('json', driver, fields=('first_name', 'last_name',
#                                                                                   'created_at', 'updated_at',)))
#
#             return JsonResponse(serialized, safe=False)
#         except ValueError:
#             return HttpResponseBadRequest('Bad request')

