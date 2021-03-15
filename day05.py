import pytest
import click
import re
from typing import Dict


@pytest.mark.parametrize(
    "test_line, expected",
    [
        ("BFFFBBFRRR", {"row": 70, "col": 7, "seat_id": 567}),
        ("FFFBBBFRRR", {"row": 14, "col": 7, "seat_id": 119}),
        ("BBFFBBFRLL", {"row": 102, "col": 4, "seat_id": 820}),
    ],
)
def test_compute_line(test_line, expected):
    assert compute_line(test_line) == expected


def get_input_data_list_from_file(filename: str) -> list:
    with open(filename) as f:
        return f.read().splitlines()


def compute_line(line: str) -> Dict[str, int]:
    row, col, seat_id = [0, 0, 0]

    litteral = line.translate(str.maketrans("FBLR", "0101"))

    row = int(litteral[:7], base=2)
    col = int(litteral[-3:], base=2)
    seat_id = row * 8 + col

    return {"row": row, "col": col, "seat_id": seat_id}


@click.command()
@click.argument("filename")
def main(filename):
    input_data = get_input_data_list_from_file(filename)
    high_seat_id = 0
    seat_data = []

    for line in input_data:
        line_dict = compute_line(line)
        high_seat_id = line_dict["seat_id"] if line_dict["seat_id"] > high_seat_id else high_seat_id
        seat_data.append(line_dict)
        seat_data.sort(key=lambda seat: seat["seat_id"])

    print(f"highest seat ID on a boarding pass (PART 1): {high_seat_id}")

    for i in range(len(seat_data) - 1):
        if seat_data[i + 1]["seat_id"] == seat_data[i]["seat_id"] + 2:
            print(seat_data[i])
            print(seat_data[i + 1])
            my_seat_id = seat_data[i]["seat_id"] + 1

    print(f"the ID of my seat (PART 2): {my_seat_id}")


if __name__ == "__main__":
    main()
