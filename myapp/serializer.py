from rest_framework import serializers

from .models import Vehicle, Driver


class DriverSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format='%d/%m/%Y %H:%M:%S', required=False)
    updated_at = serializers.DateTimeField(format='%d/%m/%Y %H:%M:%S', required=False)

    class Meta:
        model = Driver
        fields = ('pk', 'first_name', 'last_name', 'created_at', 'updated_at',)


class VehicleSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format='%d/%m/%Y %H:%M:%S', required=False)
    updated_at = serializers.DateTimeField(format='%d/%m/%Y %H:%M:%S', required=False)
    make = serializers.CharField(required=False)
    model = serializers.CharField(required=False)
    plate_number = serializers.CharField(required=False)

    class Meta:
        model = Vehicle
        fields = ['pk', 'driver_id', 'make', 'model', 'plate_number', 'created_at', 'updated_at']
