from datetime import datetime

from django.http import JsonResponse, HttpResponseBadRequest
from rest_framework.views import APIView

from .models import Driver, Vehicle
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
        else:
            data = Driver.objects.all()
            data = DriverSerializer(data, many=True)
            return JsonResponse(data.data, safe=False)  # TODO DEFAULT GET METHOD AND OTHERS???????????
