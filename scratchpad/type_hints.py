def add_three(x: int) -> int:
    return x + 3


def main() -> None:
    var = 1
    print(f"var = {add_three(var)}")


if "__main__" == __name__:
    main()
