from datetime import datetime

from django.http import JsonResponse, HttpResponseBadRequest
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Driver, Vehicle
from .serializer import DriverSerializer, VehicleSerializer


class DriverViewSet(ModelViewSet):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer

    def list(self, request, *args, **kwargs):
        created_at_gte = self.request.query_params.get('created_at__gte')
        created_at_lte = self.request.query_params.get('created_at__lte')
        if created_at_gte is not None:
            try:
                self.queryset = self.queryset.filter(created_at__gte=datetime.strptime(created_at_gte, '%d-%m-%Y'))
            except ValueError:
                return HttpResponseBadRequest('Bad request')
        if created_at_lte is not None:
            try:
                self.queryset = self.queryset.filter(created_at__lte=datetime.strptime(created_at_lte, '%d-%m-%Y'))
            except ValueError:
                return HttpResponseBadRequest('Bad request')
        drivers = DriverSerializer(self.queryset, many=True)
        return Response(drivers.data)

    def retrieve(self, request, *args, **kwargs):
        driver_id = kwargs['pk']
        if driver_id is not None:
            try:
                self.queryset = self.queryset.get(pk=driver_id)
                drivers = DriverSerializer(self.queryset, many=False)
                return JsonResponse(drivers.data, safe=False)
            except Exception as e:
                return HttpResponseBadRequest(f'Exception: {e}')

        drivers = DriverSerializer(self.queryset, many=True)
        return JsonResponse(drivers.data, safe=False)

    def create(self, request, *args, **kwargs):
        try:
            return super(DriverViewSet, self).create(request, args, kwargs)
        except Exception as e:
            return HttpResponseBadRequest(f'Exception: {e}')

    def partial_update(self, request, *args, **kwargs):
        try:
            kwargs['partial'] = True
            return super(DriverViewSet, self).partial_update(request, *args, **kwargs)
        except Exception as e:
            return HttpResponseBadRequest(f'Exception: {e}')

    def destroy(self, request, *args, **kwargs):
        try:
            obj = self.queryset.get(pk=kwargs['pk'])
        except Exception as e:
            return HttpResponseBadRequest(f'Exception: {e}')
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class VehicleViewSet(ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

    def list(self, request, *args, **kwargs):
        with_drivers = self.request.query_params.get('with_drivers')
        if with_drivers is not None and with_drivers == 'yes':
            self.queryset = self.queryset.filter(driver_id__isnull=False)
        elif with_drivers is not None and with_drivers == 'no':
            self.queryset = self.queryset.filter(driver_id__isnull=True)

        vehicle_list = VehicleSerializer(self.queryset, many=True)
        return Response(vehicle_list.data)

    def retrieve(self, request, *args, **kwargs):
        vehicle_id = kwargs['pk']
        if vehicle_id is not None:
            try:
                self.queryset = self.queryset.get(pk=vehicle_id)
                vehicle = VehicleSerializer(self.queryset, many=False)
                return JsonResponse(vehicle.data, safe=False)
            except Exception as e:
                return HttpResponseBadRequest(f'Exception: {e}')

    def create(self, request, *args, **kwargs):
        try:
            return super(VehicleViewSet, self).create(request, args, kwargs)
        except Exception as e:
            return HttpResponseBadRequest(f'Exception: {e}')

    def partial_update(self, request, *args, **kwargs):
        try:
            kwargs['partial'] = True
            return super(VehicleViewSet, self).partial_update(request, args, kwargs)
        except Exception as e:
            return HttpResponseBadRequest(f'Exception: {e}')

    def destroy(self, request, *args, **kwargs):
        try:
            return super(VehicleViewSet, self).destroy(request, args, kwargs)
        except Exception as e:
            return HttpResponseBadRequest(f'Exception: {e}')


class VehicleDriverViewSet(ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

    def set_driver(self, request, *args, **kwargs):
        try:
            vehicle = self.queryset.get(pk=kwargs['pk'])
            if 'driver_id' in request.data:
                driver_obj = Driver.objects.get(pk=request.data['driver_id'])
                vehicle.driver = driver_obj
                vehicle.save()
            else:
                vehicle.driver = None
                vehicle.save()
            serialized = VehicleSerializer(vehicle, many=False)
            return Response(serialized.data, status=status.HTTP_200_OK)
        except Exception as e:
            return HttpResponseBadRequest(f'Exception: {e}')
