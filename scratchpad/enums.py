from enum import Enum


class Month(Enum):
    JAN = "January"
    FEB = "February"
    MAR = "March"
    APR = "April"
    MAY = "May"
    JUN = "June"
    JUL = "July"
    AUG = "August"
    SEP = "September"
    OCT = "October"
    NOV = "November"
    DEC = "December"


def is_birthday(month: Month):
    return month == Month.JAN


def birthday_month_year() -> tuple[Month, int]:
    return Month.JAN, 1988


def main() -> None:
    print(f"Is January my birthday month? {is_birthday(Month.JAN)}")
    print(birthday_month_year())
    my_month, my_year = birthday_month_year()
    print(f"I was born in {my_month.value} of {my_year}")


if "__main__" == __name__:
    main()
