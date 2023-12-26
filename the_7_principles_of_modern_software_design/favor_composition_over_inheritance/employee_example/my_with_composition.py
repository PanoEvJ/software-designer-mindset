"""
Very advanced Employee management system.
"""

from dataclasses import dataclass


@dataclass
class Commission:
    commission: int = 10000
    contracts_landed: float = 0

    def compute_commission_payment(self) -> int:
        return int(self.commission * self.contracts_landed)


@dataclass
class HourlyEmployee:
    name: str
    id: int
    pay_rate: int = 0
    hours_worked: float = 0
    employer_cost: int = 100000

    def compute_pay(self, commission: Commission) -> int:
        total = int(self.pay_rate * self.hours_worked + self.employer_cost)
        if commission:
            total += commission.compute_commission_payment()
        return total


@dataclass
class SalariedEmployee:
    name: str
    id: int
    monthly_salary: int = 0
    percentage: float = 1

    def compute_pay(self, commission: Commission) -> int:
        total = int(self.monthly_salary * self.percentage)
        if commission:
            total += commission.compute_commission_payment()
        return total


@dataclass
class Freelancer:
    name: str
    id: int
    pay_rate: int = 0
    hours_worked: float = 0
    vat_number: str = ""

    def compute_pay(self, commission: Commission) -> int:
        total = int(self.pay_rate * self.hours_worked)
        if commission:
            total += commission.compute_commission_payment()
        return total


def main() -> None:
    henry = HourlyEmployee(name="Henry", id=12346, pay_rate=5000, hours_worked=100)
    henry_commission = Commission(contracts_landed=5)
    print(f"{henry.name} earned ${(henry.compute_pay(henry_commission) / 100):.2f}.")

    sarah = SalariedEmployee(name="Sarah", id=47832, monthly_salary=5000000)
    sarah_commission = Commission(contracts_landed=10)
    print(f"{sarah.name} earned ${(sarah.compute_pay(sarah_commission) / 100):.2f}.")


if __name__ == "__main__":
    main()
