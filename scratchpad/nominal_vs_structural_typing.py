class Book:
    def __init__(self, title: str, author: str, pages: int) -> None:
        self.title = title
        self.author = author
        self.pages = pages

    def __len__(self) -> int:
        return self.pages


def main() -> None:
    my_str = "Hello"
    print(len(my_str))
    my_list = [1, 2, 3]
    print(len(my_list))
    my_dict = {"a": 1, "b": 2}
    print(len(my_dict))
    my_book = Book("War and Peace", "Leo Tolstoy", 1225)
    print(len(my_book))


if "__main__" == __name__:
    main()
