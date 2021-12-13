from rest_framework import status
from rest_framework.test import APITestCase

from .models import *


class DriverTests(APITestCase):
    def setUp(self) -> None:
        Driver.objects.create(first_name='test', last_name='TEST')
        Driver.objects.create(first_name='foo', last_name='bar')

    def test_get_drivers_list(self):
        response = self.client.get('/drivers/driver/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 2)

    def test_date_filter_gte(self):
        response_gte = self.client.get('/drivers/driver/?created_at__gte=10-11-2021')
        self.assertEqual(response_gte.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response_gte.json()), 2)

    def test_date_filter_lte(self):
        response_lte = self.client.get('/drivers/driver/?created_at__lte=10-11-2021')
        self.assertEqual(response_lte.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response_lte.json()), 0)

    def test_get_driver_by_id(self):
        response = self.client.get('/drivers/driver/1/')
        self.assertEqual(response.json()['first_name'], 'test')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update(self):
        data = {"first_name": "partial update"}
        response = self.client.patch('/drivers/driver/1/', data=data)
        self.assertEqual(response.json()['first_name'], 'partial update')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_driver(self):
        data = {"first_name": "POST",
                "last_name": "CREATE"}
        response = self.client.post('/drivers/driver/', data=data)
        self.assertEqual(Driver.objects.count(), 3)
        self.assertEqual(response.json()['pk'], 3)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_delete_driver(self):
        response = self.client.delete('/drivers/driver/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Driver.objects.count(), 1)


class VehicleTests(APITestCase):
    def setUp(self) -> None:
        Vehicle.objects.create(make='foo make', model='bar model', plate_number='AA1111AA')
        Vehicle.objects.create(make='test', model='test', plate_number='AA9999AA')
        Driver.objects.create(first_name='Driver', last_name='Vehicle')

    def test_get_vehicles_list(self):
        response = self.client.get('/vehicles/vehicle/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 2)

    def test_with_driver_filter(self):
        response = self.client.get('/vehicles/vehicle/?with_drivers=yes')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 0)

    def test_without_driver_filter(self):
        response = self.client.get('/vehicles/vehicle/?with_drivers=no')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 2)

    def test_get_vehicle_by_id(self):
        response = self.client.get('/vehicles/vehicle/1/')
        self.assertEqual(response.json()['make'], 'foo make')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_vehicle(self):
        data = {
            'make': 'example make',
            'model': 'example model',
            'plate_number': 'TE0000ST'
        }
        response = self.client.post('/vehicles/vehicle/', data=data)
        self.assertEqual(Vehicle.objects.count(), 3)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json()['plate_number'], 'TE 0000 ST')

    def test_update_vehicle(self):
        data = {'make': 'toyota'}
        response = self.client.patch('/vehicles/vehicle/1/', data=data)
        self.assertEqual(response.json()['make'], 'toyota')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_set_driver(self):
        data = {'driver_id': 1}
        response = self.client.post('/vehicles/set_driver/1/', data=data)
        self.assertEqual(response.json()['driver_id'], 1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_unset_driver(self):
        response = self.client.post('/vehicles/set_driver/1/')
        self.assertEqual(response.json()['driver_id'], None)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_vehicle(self):
        response = self.client.delete('/vehicles/vehicle/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Vehicle.objects.count(), 1)