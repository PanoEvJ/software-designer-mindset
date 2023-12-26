"""
Very advanced Employee management system.
"""

from dataclasses import dataclass, field
from typing import Protocol


class PaymentSource(Protocol):
    def compute_pay(self) -> int:
        ...


@dataclass
class HourlyPayment:
    pay_rate: int
    hours_worked: float = 0
    employer_cost: int = 100000

    def compute_pay(
        self,
    ) -> int:
        return int(self.pay_rate * self.hours_worked + self.employer_cost)


@dataclass
class SalaryPayment:
    monthly_salary: int
    percentage: float = 1

    def compute_pay(
        self,
    ) -> int:
        return int(self.monthly_salary * self.percentage)


@dataclass
class CommissionPayment:
    commission: int = 10000
    contracts_landed: float = 0

    def compute_pay(self) -> int:
        return int(self.commission * self.contracts_landed)


@dataclass
class Employee:
    name: str
    id: int
    payment_sources: list[PaymentSource] = field(default_factory=list)

    def add_payment_source(self, payment_source: PaymentSource):
        self.payment_sources.append(payment_source)

    def compute_pay(self) -> int:
        total: int = 0
        for source in self.payment_sources:
            total += source.compute_pay()
        return total


def main() -> None:
    henry = Employee(name="Henry", id=12346)
    henry_hourly_payment = HourlyPayment(pay_rate=5000, hours_worked=100)
    henry_commission_payment = CommissionPayment(contracts_landed=5)
    henry.add_payment_source(payment_source=henry_hourly_payment)
    henry.add_payment_source(payment_source=henry_commission_payment)
    print(f"{henry.name} earned ${(henry.compute_pay() / 100):.2f}.")

    sarah = Employee(name="Sarah", id=47832)
    sarah_salary_payment = SalaryPayment(monthly_salary=5000000)
    sarah_commission_payment = CommissionPayment(contracts_landed=10)
    sarah.add_payment_source(payment_source=sarah_salary_payment)
    sarah.add_payment_source(payment_source=sarah_commission_payment)
    print(f"{sarah.name} earned ${(sarah.compute_pay() / 100):.2f}.")


if __name__ == "__main__":
    main()
