from enum import Enum


def get_rental_days() -> int:
    days = 0
    while days < 1:
        days_str = input(
            "How many days would you like to rent the vehicle? (enter a positive number) "
        )
        try:
            days = int(days_str)
        except ValueError:
            print("Invalid input. Please enter a number.")
    return days


def get_rental_kms() -> int:
    km = 0
    while km < 1:
        km_str = input(
            "How many kilometers would you like to drive (enter a positive number)? "
        )
        try:
            km = int(km_str)
        except ValueError:
            print("Invalid input. Please enter a number.")

    # subtract the base number of kms
    km = max(km - 100, 0)
    return km


class VehicleType(Enum):
    VW = "vw"
    BMW = "bmw"
    FORD = "ford"


def get_vehicle_type() -> str:
    vehicle_type = ""
    while vehicle_type not in VehicleType:
        vehicle_type = input(
            "What type of vehicle would you like to rent (choose vw, bmw, or ford)? "
        )
    return vehicle_type


vehicle_data = {
    "vw": {"price_per_km": 30, "price_per_day": 6000},
    "bmw": {"price_per_km": 35, "price_per_day": 8500},
    "ford": {"price_per_km": 25, "price_per_day": 12000},
}


def compute_rental_cost(vehicle_type: str, days: int, km: int) -> int:
    price_per_km = vehicle_data[vehicle_type]["price_per_km"]
    price_per_day = vehicle_data[vehicle_type]["price_per_day"]
    paid_kms = max(km - 100, 0)
    return price_per_km * paid_kms + price_per_day * days


def main():
    print("Vehicle Rental before")

    days = get_rental_days()
    km = get_rental_kms()
    vehicle_type = get_vehicle_type()

    rental_price = compute_rental_cost(vehicle_type, days, km)

    # print the result
    print(f"The total price of the rental is ${(rental_price / 100):.2f}")


if __name__ == "__main__":
    main()
