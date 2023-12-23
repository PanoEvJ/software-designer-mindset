from dataclasses import dataclass, field
from enum import Enum


class PhoneBrand(Enum):
    IPHONE = "iPhone"
    SAMSUNG = "Samsung"


class PhoneModel(Enum):
    IPHONE_11 = "iPhone 11"
    IPHONE_11_PRO = "iPhone 11 Pro"
    IPHONE_11_PRO_MAX = "iPhone 11 Pro Max"
    IPHONE_XS = "iPhone XS"
    IPHONE = "iPhone"
    GALAXY_S10 = "Galaxy S10"
    GALAXY_S10_PLUS = "Galaxy S10+"
    GALAXY_S10E = "Galaxy S10e"
    GALAXY_S9 = "Galaxy S9"
    GALAXY_S = "Galaxy S"


@dataclass(frozen=True)
class Customer:
    name: str
    address: str
    phone_number: str
    email: str
    notes: str = field(default="")


@dataclass(frozen=True)
class Phone:
    number: str
    phone_brand: PhoneBrand
    phone_model: PhoneModel
    price: float
    serial_number: str


@dataclass(frozen=True)
class Plan:
    name: str
    monthly_price: float
    total_number_of_months: int
    data: int
    minutes: int
    messages: int
    customer: Customer
    phone: Phone
    is_phone_included: bool = False
