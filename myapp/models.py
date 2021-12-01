from django.db import models


class Driver(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'ID: {self.pk}. {self.first_name} {self.last_name}'


class Vehicle(models.Model):
    driver_id = models.ForeignKey('Driver', on_delete=models.PROTECT)
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    plate_number = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Vehicle ID:{self.pk}.\n' \
               f'Driver ID:{self.driver_id}.\n' \
               f'{self.make}, {self.model}, number: {self.plate_number}'
