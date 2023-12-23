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


def main() -> None:
    print(f"Is January my birthday month? {is_birthday(Month.JAN)}")
    print(Month.JAN.value)


if "__main__" == __name__:
    main()
