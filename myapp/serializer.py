from rest_framework import serializers

from .models import Vehicle, Driver


class DriverSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format='%d/%m/%Y %H:%M:%S')
    updated_at = serializers.DateTimeField(format='%d/%m/%Y %H:%M:%S')

    class Meta:
        model = Driver
        fields = ('pk', 'first_name', 'last_name', 'created_at', 'updated_at',)


class VehicleSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format='%d/%m/%Y %H:%M:%S')
    updated_at = serializers.DateTimeField(format='%d/%m/%Y %H:%M:%S')

    class Meta:
        model = Vehicle
        fields = ['pk', 'driver_id_id', 'make', 'model', 'plate_number', 'created_at', 'updated_at']
