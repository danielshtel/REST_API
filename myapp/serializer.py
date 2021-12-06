from .models import Vehicle, Driver
from rest_framework import serializers


class DriverSerializer(serializers.HyperlinkedModelSerializer):
    created_at = serializers.DateTimeField(format='%d/%m/%Y %H:%M:%S')
    updated_at = serializers.DateTimeField(format='%d/%m/%Y %H:%M:%S')
    class Meta:
        model = Driver
        fields = ['first_name', 'last_name', 'created_at', 'updated_at']


class VehicleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vehicle
        fields = ['driver_id', 'make', 'model', 'plate_number', 'created_at', 'updated_at']
