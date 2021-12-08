import json
from datetime import datetime
from dataclasses import dataclass
from django.http import JsonResponse, HttpResponseBadRequest
from rest_framework.views import APIView

from .models import Driver, Vehicle
from .serializer import DriverSerializer


class DriverViewSet(APIView):
    drivers_queryset = Driver.objects.all()
    serializer_class = DriverSerializer

    def get(self, request, *args, **kwargs):
        created_at_gte = self.request.query_params.get('created_at__gte')
        created_at_lte = self.request.query_params.get('created_at__lte')
        if created_at_gte is not None:
            try:
                self.drivers_queryset = self.drivers_queryset.filter(
                    created_at__gte=datetime.strptime(created_at_gte, '%d-%m-%Y')
                )
            except ValueError:
                return HttpResponseBadRequest('Bad request')

        if created_at_lte is not None:
            try:
                self.drivers_queryset = self.drivers_queryset.filter(
                    created_at__lte=datetime.strptime(created_at_lte, '%d-%m-%Y')
                )
            except ValueError:
                return HttpResponseBadRequest('Bad request')

        drivers = DriverSerializer(self.drivers_queryset, many=True)
        return JsonResponse(drivers.data, safe=False)

    def post(self, request):
        try:
            data = json.loads(request.body)
            new_driver = Driver(first_name=data['first_name'], last_name=data['last_name'])
            new_driver.save()
            serialized_driver = DriverSerializer(new_driver)
            return JsonResponse(serialized_driver.data, safe=False)
        except Exception as e:
            return HttpResponseBadRequest(f'Exception: {e}')


class DriverCRUDSet(APIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer

    def get(self, request, *args, **kwargs):
        try:
            self.queryset = Driver.objects.get(pk=kwargs['driver_id'])
            driver = DriverSerializer(self.queryset)
            return JsonResponse(driver.data, safe=False)
        except Exception as e:
            return HttpResponseBadRequest(f'Exception: {e}')

    def put(self, request, *args, **kwargs):
        data = json.loads(request.body)
        self.queryset = Driver.objects.get(pk=kwargs['driver_id'])
        self.queryset.save()
        upd_driver = DriverSerializer(self.queryset)
        return JsonResponse(upd_driver.data) # TODO Validate json and keywords using dataclasses?


# @dataclass
# class DriverData:
#     first_name: str = None
#     last_name: str = None


# driver_data = user_data = DriverData(**dict_from_json)