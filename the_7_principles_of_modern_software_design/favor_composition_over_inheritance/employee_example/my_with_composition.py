"""
Very advanced Employee management system.
"""

from dataclasses import dataclass
from typing import Protocol


class PaymentSources(Protocol):
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

    def compute_pay(self, payment_sources: list[PaymentSources]) -> int:
        total: int = 0
        for source in payment_sources:
            total += source.compute_pay()
        return total


def main() -> None:
    henry = Employee(name="Henry", id=12346)
    henry_hourly_payment = HourlyPayment(pay_rate=5000, hours_worked=100)
    henry_commission_payment = CommissionPayment(contracts_landed=5)
    print(
        f"{henry.name} earned ${(henry.compute_pay([henry_hourly_payment, henry_commission_payment]) / 100):.2f}."
    )

    sarah = Employee(name="Sarah", id=47832)
    sarah_salary_payment = SalaryPayment(monthly_salary=5000000)
    sarah_commission_payment = CommissionPayment(contracts_landed=10)
    print(
        f"{sarah.name} earned ${(sarah.compute_pay([sarah_salary_payment, sarah_commission_payment]) / 100):.2f}."
    )


if __name__ == "__main__":
    main()
