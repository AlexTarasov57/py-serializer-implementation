import json

from car.models import Car
from car.serializers import CarSerializer


def serialize_car_object(car: Car) -> bytes:
    serializer = CarSerializer(car)
    return json.dumps(serializer.data)


def deserialize_car_object(json: bytes) -> Car:
    data = json.loads(json)
    serializer = CarSerializer(data=data)
    if serializer.is_valid():
        return Car(**serializer.validated_data)
    raise ValueError(serializer.errors)
