import pytest
import click
import re
from typing import List, Optional, Dict, Any
from copy import copy
from itertools import combinations

test_data = """35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576"""

premamble_len = 25


def get_input_data_list_from_file(filename: str) -> str:
    with open(filename) as f:
        return f.read()


def number_is_valid(premamble, number):
    for x, y in combinations(premamble, 2):
        if x + y == number:
            return True

    return False


@click.command()
@click.argument("filename")
def main(filename):
    input_data = get_input_data_list_from_file(filename)

    data = list(map(int, input_data.splitlines()))
    # data = list(map(int, test_data.splitlines()))

    try:
        for i in range(premamble_len, len(data)):
            premamble = data[i - premamble_len : i]
            current_number = data[i]

            assert number_is_valid(premamble, current_number)
    except AssertionError:
        print(f"(part 1): {current_number}")

    x = 0
    y = 1

    while True:
        data_slice = data[x:y]
        data_slice_sum = sum(data_slice)

        if data_slice_sum == current_number:
            weakness = min(data_slice) + max(data_slice)
            break

        if data_slice_sum > current_number:
            x += 1

        if data_slice_sum < current_number:
            y += 1

    print(f"(part 2): {weakness}")


if __name__ == "__main__":
    main()
