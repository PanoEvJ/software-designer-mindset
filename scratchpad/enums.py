from enum import Enum, auto


class Month(Enum):
    JAN = auto()
    FEB = auto()
    MAR = auto()
    APR = auto()
    MAY = auto()
    JUN = auto()
    JUL = auto()
    AUG = auto()
    SEP = auto()
    OCT = auto()
    NOV = auto()
    DEC = auto()


def is_birthday(month: Month):
    return month == Month.JAN


def main() -> None:
    print(f"Is January my birthday month? {is_birthday(Month.JAN)}")
    print(Month.JAN.value)


if "__main__" == __name__:
    main()
