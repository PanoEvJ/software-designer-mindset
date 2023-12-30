from enum import Enum, auto


class PaymentStatus(Enum):
    """Payment status"""

    OPEN = auto()
    PAID = auto()


class Order:
    def __init__(self):
        self.items: list[str] = []
        self.quantities: list[int] = []
        self.prices: list[int] = []
        self.status: str = "open"

    def add_item(self, name: str, quantity: int, price: int) -> None:
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)

    def compute_total_price(self) -> None:
        total = 0
        for i in range(len(self.prices)):
            total += self.quantities[i] * self.prices[i]
        print(f"The total price is: ${(total / 100):.2f}.")


def main() -> None:
    order = Order()
    order.add_item("Keyboard", 1, 5000)
    order.add_item("SSD", 1, 15000)
    order.add_item("USB cable", 2, 500)

    order.compute_total_price()


if __name__ == "__main__":
    main()
