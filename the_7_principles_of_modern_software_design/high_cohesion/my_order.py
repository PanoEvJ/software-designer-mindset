from dataclasses import dataclass
from enum import Enum, auto


class PaymentStatus(Enum):
    OPEN = auto()
    PAID = auto()


class Order:
    def __init__(self):
        self.items: list[str] = []
        self.quantities: list[int] = []
        self.prices: list[int] = []
        self.status: PaymentStatus = PaymentStatus.OPEN

    def add_item(self, name: str, quantity: int, price: int) -> None:
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)


@dataclass
class PaymentProcessor:
    order: Order
    security_code: str

    def pay_debit(self) -> None:
        print("Processing debit payment type")
        print(f"Verifying security code: {self.security_code}")
        self.order.status = PaymentStatus.PAID

    def pay_credit(self) -> None:
        print("Processing credit payment type")
        print(f"Verifying security code: {self.security_code}")
        self.order.status = PaymentStatus.PAID


def main() -> None:
    order = Order()
    order.add_item("Keyboard", 1, 5000)
    order.add_item("SSD", 1, 15000)
    order.add_item("USB cable", 2, 500)

    payment = PaymentProcessor(order=order, security_code="0372846")
    payment.pay_debit()


if __name__ == "__main__":
    main()
