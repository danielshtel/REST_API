from datetime import datetime

from rest_framework import generics
from django.http import JsonResponse, HttpResponseBadRequest

from .serializer import DriverSerializer
from .models import Driver


class DriverViewSet(generics.ListAPIView):
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
