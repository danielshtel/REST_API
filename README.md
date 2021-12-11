# REST API for drivers park.

REST-API application for managing drivers and vehicles data.

#### Created by:

* <https://t.me/Daniel_Daniel97>
* daniillevchenko98@gmail.com

# Drivers:

## Get the list of drivers

### Request

`GET /drivers/driver/`

### Response

```
HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "pk": 1,
        "first_name": "Stepanenko",
        "last_name": "Valentina",
        "created_at": "02/12/2021 11:16:04",
        "updated_at": "09/12/2021 13:18:34"
    },
    {
        "pk": 4,
        "first_name": "sergey",
        "last_name": "levchenko",
        "created_at": "08/12/2021 17:11:36",
        "updated_at": "08/12/2021 17:11:36"
    }
]
```

## Get drivers filtered by date

### Request

`GET /drivers/driver/?created_at__gte=10-11-2021`

### Response

```
HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "pk": 1,
        "first_name": "Stepanenko",
        "last_name": "Valentina",
        "created_at": "02/12/2021 11:16:04",
        "updated_at": "09/12/2021 13:18:34"
    }
]
```

### Request

`GET /drivers/driver/?created_at__lte=16-11-2021`

### Response

```
HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[]
```

## Get driver by id

### Request

`GET /drivers/driver/1/`

### Response

```
HTTP 200 OK
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "pk": 1,
    "first_name": "Stepanenko",
    "last_name": "Valentina",
    "created_at": "02/12/2021 11:16:04",
    "updated_at": "09/12/2021 13:18:34"
}
```

## Create new driver

### Request

`POST /drivers/driver/`

### Response

```
HTTP 201 Created
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "pk": 30,
    "first_name": "foo",
    "last_name": "bar",
    "created_at": "11/12/2021 16:36:28",
    "updated_at": "11/12/2021 16:36:28"
}
```

## Update driver

### Request

`PATCH /drivers/driver/30/ `

### Response

```
HTTP 200 OK
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "pk": 30,
    "first_name": "updated name",
    "last_name": "bar",
    "created_at": "11/12/2021 16:36:28",
    "updated_at": "11/12/2021 16:38:35"
}
```

## Delete driver

### Request

`DELETE /drivers/driver/30/`

### Response

```
HTTP 204 No Content
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept
```

# Vehicles:

## Get the list of vehicles

### Request

`GET /vehicles/vehicle`

### Response

```
HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "pk": 1,
        "driver_id": 1,
        "make": "Renault",
        "model": "Megane2",
        "plate_number": "BI 1662 BE",
        "created_at": "02/12/2021 14:14:16",
        "updated_at": "10/12/2021 19:40:07"
    },
    {
        "pk": 2,
        "driver_id": 1,
        "make": "Toyota",
        "model": "Camry",
        "plate_number": "BI 6883 AA",
        "created_at": "09/12/2021 14:07:55",
        "updated_at": "09/12/2021 14:07:55"
    }
]
```

## Get vehicles with or w/o drivers

### Request

`GET /vehicles/vehicle/?with_drivers=yes`

### Response

```
HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "pk": 1,
        "driver_id": 1,
        "make": "Renault",
        "model": "Megane2",
        "plate_number": "BI 1662 BE",
        "created_at": "02/12/2021 14:14:16",
        "updated_at": "10/12/2021 19:40:07"
    },
    {
        "pk": 2,
        "driver_id": 1,
        "make": "Toyota",
        "model": "Camry",
        "plate_number": "BI 6883 AA",
        "created_at": "09/12/2021 14:07:55",
        "updated_at": "09/12/2021 14:07:55"
    }
]
```

### Request

`GET /vehicles/vehicle/?with_drivers=no`

### Response

```

HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "pk": 4,
        "driver_id": null,
        "make": "bmw",
        "model": "i38",
        "plate_number": "АА 9999 АА",
        "created_at": "10/12/2021 17:55:48",
        "updated_at": "10/12/2021 20:52:00"
    }
]
```

## Get vehicle by id

### Request

`GET /vehicles/vehicle/1`

### Response

```
HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "pk": 1,
    "driver_id": 1,
    "make": "Renault",
    "model": "Megane2",
    "plate_number": "BI 1662 BE",
    "created_at": "02/12/2021 14:14:16",
    "updated_at": "10/12/2021 19:40:07"
}
```

## Create new vehicle

### Request

`POST /vehicles/vehicle/`

### Response

```
HTTP 201 Created
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "pk": 9,
    "driver_id": null,
    "make": "foo",
    "model": "bar",
    "plate_number": "AA 1111 AA",
    "created_at": "11/12/2021 16:57:26",
    "updated_at": "11/12/2021 16:57:26"
}
```

## Update vehicle

### Request

`PATCH /vehicles/vehicle/9/`

### Response

```
HTTP 200 OK
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "pk": 9,
    "driver_id": null,
    "make": "test update",
    "model": "bar",
    "plate_number": "AA 1111 AA",
    "created_at": "11/12/2021 16:57:26",
    "updated_at": "11/12/2021 16:59:16"
}
```

## Set / unset driver into vehicle

### Request

`POST /vehicles/set_driver/9/`

##### Request body

```
{"driver_id":1}
```

### Response

```
HTTP 200 OK
Allow: POST, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "pk": 9,
    "driver_id": 1,
    "make": "test update",
    "model": "bar",
    "plate_number": "AA 1111 AA",
    "created_at": "11/12/2021 16:57:26",
    "updated_at": "11/12/2021 17:04:51"
}
```

### Request

`POST /vehicles/set_driver/9/`

### Response

```
HTTP 200 OK
Allow: POST, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "pk": 9,
    "driver_id": null,
    "make": "test update",
    "model": "bar",
    "plate_number": "AA 1111 AA",
    "created_at": "11/12/2021 16:57:26",
    "updated_at": "11/12/2021 17:07:41"
}
```

## Delete vehicle

### Request

`DELETE /vehicles/vehicle/9/`

### Response

```
HTTP 204 No Content
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept
```
