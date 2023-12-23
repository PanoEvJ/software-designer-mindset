from typing import Callable

IntFunction = Callable[[int], int]


def add_three(x: int) -> int:
    return x + 3


def main() -> None:
    var = 1
    my_var: IntFunction = add_three
    print(f"var = {my_var(var)}")


if "__main__" == __name__:
    main()
