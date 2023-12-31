from typing import Callable

from pos.authorization import authorize_google, authorize_sms
from pos.order import Order
from pos.payment import (
    CreditPaymentProcessor,
    DebitPaymentProcessor,
    PaymentProcessor,
    PaypalPaymentProcessor,
)


def read_choice(question: str, choices: list[str]) -> str:
    choice = ""
    while choice not in choices:
        choice = input(f"{question} ({', '.join(choices)})? ")
    return choice


def create_debit_payment_processor() -> PaymentProcessor:
    return DebitPaymentProcessor()


def create_paypal_payment_processor() -> PaymentProcessor:
    email_address = input("Enter your email address: ")
    return PaypalPaymentProcessor(email_address=email_address)


def create_credit_payment_processor() -> PaymentProcessor:
    security_code = input("Enter the security code: ")
    return CreditPaymentProcessor(security_code=security_code)


PAYMENTS: dict[str, Callable[[], PaymentProcessor]] = {
    "paypal": create_paypal_payment_processor,
    "credit": create_credit_payment_processor,
    "debit": create_debit_payment_processor,
}


def payment_factory() -> PaymentProcessor:
    payment_choice = read_choice(
        "How would you like to pay?", ["paypal", "credit", "debit"]
    )
    return PAYMENTS[payment_choice]()


AUTHORIZERS: dict[str, Callable[[], bool]] = {
    "google": authorize_google,
    "sms": authorize_sms,
}


def authorizer_factory() -> Callable[[], bool]:
    auth_choice = read_choice("Choose your authentication method", ["google", "sms"])
    return AUTHORIZERS[auth_choice]


def main():
    order = Order()
    order.add_item("Keyboard", 1, 5000)
    order.add_item("SSD", 1, 15000)
    order.add_item("USB cable", 2, 500)

    print(f"The total price is: ${(order.total_price / 100):.2f}.")

    # select the payment method
    processor = payment_factory()

    # select the authentication method
    auth = authorizer_factory()

    processor.pay(order, auth)


if __name__ == "__main__":
    main()
