"""
Very advanced Employee management system.
"""

from dataclasses import dataclass


@dataclass
class Employee:
    name: str
    id: int
    commission: int = 10000
    contracts_landed: float = 0

    def compute_pay(self) -> int:
        return int(self.commission * self.contracts_landed)


@dataclass
class HourlyEmployee(Employee):
    pay_rate: int = 0
    hours_worked: float = 0
    employer_cost: int = 100000

    def compute_pay(self) -> int:
        return super().compute_pay() + int(
            self.pay_rate * self.hours_worked + self.employer_cost
        )


@dataclass
class SalariedEmployee(Employee):
    monthly_salary: int = 0
    percentage: float = 1

    def compute_pay(self) -> int:
        return super().compute_pay() + int(self.monthly_salary * self.percentage)


@dataclass
class Freelancer(Employee):
    pay_rate: int = 0
    hours_worked: float = 0
    vat_number: str = ""

    def compute_pay(self) -> int:
        return super().compute_pay() + int(self.pay_rate * self.hours_worked)


def main() -> None:
    henry = HourlyEmployee(name="Henry", id=12346, pay_rate=5000, hours_worked=100)
    print(f"{henry.name} earned ${(henry.compute_pay() / 100):.2f}.")

    sarah = SalariedEmployee(
        name="Sarah", id=47832, monthly_salary=500000, contracts_landed=10
    )
    print(f"{sarah.name} earned ${(sarah.compute_pay() / 100):.2f}.")


if __name__ == "__main__":
    main()
