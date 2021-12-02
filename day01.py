import pytest
import re
from typing import List, Optional, Dict, Any, Tuple
from copy import copy

test_data = """199
200
208
210
200
207
240
269
260
263"""

expected = 7
expected2 = 5


def test_part1():
    assert part1(massage_data(test_data.splitlines())) == expected


def test_part2():
    assert part2(massage_data(test_data.splitlines())) == expected2


def get_input_data_list_from_file(filename: str) -> List[str]:
    with open(filename) as f:
        return f.readlines()


def part1(data: List[int]) -> int:
    count = 0
    previous_measurment = None
    for measurment in data:

        if previous_measurment == None:
            previous_measurment = measurment
            continue

        if measurment > previous_measurment:
            count += 1

        previous_measurment = measurment

    return count


def part2(data: List[int]) -> int:
    count = 0
    previous_measurment = None

    new_list = []

    for i, line in enumerate(data):
        if i + 3 > len(data):
            break

        _sum = sum(data[i : i + 3])

        new_list.append(_sum)

    count = part1(new_list)

    return count


def massage_data(data: List[str]) -> List[int]:
    return [int(x) for x in data]


def main():

    input_data = massage_data(get_input_data_list_from_file("input01.txt"))

    count = part1(input_data)
    count2 = part2(input_data)

    print(f"(part 1): {count}")
    print(f"(part 2): {count2}")


if __name__ == "__main__":
    main()
