from dataclasses import dataclass
from enum import Enum, auto


class FuelType(Enum):
    PETROL = auto()
    DIESEL = auto()
    ELECTRIC = auto()


class TruckCabStyle(Enum):
    REGULAR = auto()
    EXTENDED = auto()
    CREW = auto()


class VehicleType:
    pass


class Price:
    pass


@dataclass
class Car(VehicleType):
    number_of_seats: int
    storage_capacity_litres: int


@dataclass
class Trailer(VehicleType):
    capacity_m3: int
    price_per_month: int


@dataclass
class Truck(VehicleType):
    cab_style: TruckCabStyle


@dataclass
class PricePerDay(Price):
    price_per_km: int
    price_per_day: int


@dataclass
class PricePerMonth(Price):
    price_per_month: int


@dataclass
class Vehicle:
    brand: str
    model: str
    color: str
    fuel_type: FuelType
    license_plate: str
    reserved: bool
    vehicle_type: VehicleType
    price: Price


def main():
    pass


if __name__ == "__main__":
    main()
