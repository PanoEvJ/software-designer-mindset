import random
import string
from dataclasses import dataclass, field
from enum import Enum, auto


def generate_vehicle_license() -> str:
    """Helper method for generating a vehicle license number."""

    digit_part = "".join(random.choices(string.digits, k=2))
    letter_part_1 = "".join(random.choices(string.ascii_uppercase, k=2))
    letter_part_2 = "".join(random.choices(string.ascii_uppercase, k=2))
    return f"{letter_part_1}-{digit_part}-{letter_part_2}"


class Accessory(Enum):
    AIRCO = auto()
    CRUISECONTROL = auto()
    NAVIGATION = auto()
    OPENROOF = auto()
    BATHTUB = auto()
    MINIBAR = auto()


class FuelType(Enum):
    PETROL = auto()
    DIESEL = auto()
    ELECTRIC = auto()


@dataclass(frozen=True)
class Vehicle:
    brand: str
    model: str
    color: str
    license_plate: str = field(default_factory=generate_vehicle_license)
    fuel_type: FuelType = FuelType.ELECTRIC
    accessories: list[Accessory] = field(
        default_factory=lambda: [Accessory.AIRCO, Accessory.NAVIGATION]
    )


def main() -> None:
    """
    Create some vehicles and print their details.
    """

    tesla = Vehicle(
        brand="Tesla",
        model="Model 3",
        color="black",
    )
    volkswagen = Vehicle(
        brand="Volkswagen",
        model="ID3",
        color="white",
        fuel_type=FuelType.DIESEL,
        accessories=[Accessory.NAVIGATION, Accessory.CRUISECONTROL],
    )
    bmw = Vehicle(
        brand="BMW",
        model="520e",
        color="blue",
        license_plate=generate_vehicle_license(),
        fuel_type=FuelType.PETROL,
        accessories=[Accessory.OPENROOF],
    )

    print(tesla)
    print(volkswagen)
    print(bmw)


if __name__ == "__main__":
    main()
