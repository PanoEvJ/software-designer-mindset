from dataclasses import dataclass, field
from enum import Enum, auto


class PaymentStatus(Enum):
    """Payment status"""

    OPEN = auto()
    PAID = auto()


@dataclass
class LineItem:
    item: str
    quantity: int
    price: int

    @property
    def total_price(self) -> int:
        return self.quantity * self.price

    def __post_init__(self) -> None:
        if self.quantity < 0:
            raise ValueError("Cannot have negative quantities.")
        if self.price < 0:
            raise ValueError("Cannot have negative prices.")


@dataclass
class Order:
    line_items: list[LineItem] = field(default_factory=list)

    def add_item(self, line_item: LineItem) -> None:
        self.line_items.append(line_item)

    @property
    def total_price(self) -> int:
        return sum(item.total_price for item in self.line_items)


def main() -> None:
    order = Order()
    order.add_item(LineItem("Keyboard", 1, 5000))
    order.add_item(LineItem("SSD", 1, 15000))
    order.add_item(LineItem("USB cable", 2, 500))

    print(f"The total price is: ${(order.total_price / 100):.2f}.")


if __name__ == "__main__":
    main()
