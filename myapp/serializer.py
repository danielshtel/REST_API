from .models import Vehicle, Driver
from rest_framework import serializers


class DriverSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Driver
        fields = ['first_name', 'last_name', 'created_at', 'updated_at']


class VehicleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vehicle
        fields = ['driver_id', 'make', 'model', 'plate_number', 'created_at', 'updated_at']
