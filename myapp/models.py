from django.db import models


class Driver(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.pk}'


class Vehicle(models.Model):
    driver = models.ForeignKey('Driver', on_delete=models.PROTECT, null=True)
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    plate_number = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Vehicle ID:{self.pk}.'

    def save(self, *args, **kwargs):
        if ' ' not in self.plate_number:
            self.plate_number = f'{self.plate_number[0:2]} {self.plate_number[2:6]} {self.plate_number[6:]}'
        super(Vehicle, self).save(*args, **kwargs)
