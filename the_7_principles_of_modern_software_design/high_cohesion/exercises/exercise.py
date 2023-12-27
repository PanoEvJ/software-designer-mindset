import csv
from typing import Any

Record = dict[str, Any]

INPUT_FILE = "data.csv"
OUTPUT_FILE = "processed.csv"
FIELD_NAMES_OUTPUT = ["name", "status", "is_active"]


def from_csv(filename: str) -> list[Record]:
    with open(filename, mode="r", encoding="csv") as f:
        reader = csv.DictReader(f)
        return list(reader)


def to_csv(data: list[Record], filename: str, fieldnames: list[str]) -> None:
    with open(filename, mode="w", encoding="csv") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)


def process_data(row: Record) -> Record:
    row_copy = row.copy()
    if row_copy["status"] == "active":
        row_copy["is_active"] = True
    else:
        row_copy["is_active"] = False
    return row_copy


def main() -> None:
    data = from_csv("data.csv")

    processed_data = [process_data(row) for row in data]

    to_csv(processed_data, filename="processed_data.csv", fieldnames=FIELD_NAMES_OUTPUT)


if __name__ == "__main__":
    main()
