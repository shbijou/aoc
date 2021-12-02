import pytest
import click
import re
from typing import List, Optional, Dict, Any


test_data = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags."""

test_data2 = """shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags."""


def split_bag_line(line: str) -> Dict[str, Dict[str, int]]:
    l = line.rstrip(".").split(" bags contain ")
    line_key = line.split(" bags", maxsplit=1)[0]

    l2 = l.pop(1).replace(" bag", "").split(", ")

    l3 = [i.rstrip("s") for i in l2]

    d = {}
    contains = {}

    for i in l3:
        qty, color = i.split(" ", maxsplit=1)
        if color == "other":
            contains = {}
        else:
            contains = contains | dict({color: int(qty)})
        d = d | {line_key: contains}

    return d


def check_for_bag_color(data, color: str) -> List[str]:
    found = []
    for bag_color, contains in data.items():
        if color in contains.keys():
            found.append(bag_color)

    return found


def get_input_data_list_from_file(filename: str) -> str:
    with open(filename) as f:
        return f.read()


def compute(data: Dict[Any, Any]) -> int:
    count = 0

    # look for colors
    colors_to_check = ["shiny gold"]
    checked = []
    bags_found = set()

    while len(colors_to_check):
        # always remove the first in list
        next_color = colors_to_check.pop(0)

        # don't check a color twice
        if next_color in checked:
            continue
        checked.append(next_color)

        # look for bags containing color
        colors_to_check += check_for_bag_color(data, next_color)

        for color in colors_to_check:
            bags_found.add(color)

        count = len(bags_found)

    return count


def compute_pt2(data: str) -> int:
    count = 0
    multi = [1]
    colors_to_check = ["shiny gold"]

    while len(colors_to_check):
        # always remove the first in list
        next_color = colors_to_check.pop(0)
        next_multi = multi.pop(0)

        keys = list(data[next_color].keys())
        vals = list(data[next_color].values())

        colors_to_check += keys
        multi += [i * next_multi for i in vals]

        count += sum(vals) * next_multi

    return count


@click.command()
@click.argument("filename")
def main(filename):
    input_data = get_input_data_list_from_file(filename)

    # parse the dataset
    # data_list = test_data.splitlines()
    # data_list = test_data2.splitlines()
    data_list = input_data.splitlines()
    data_dict: Dict[str, Any] = {}

    for line in data_list:
        split_list = split_bag_line(line)
        data_dict = data_dict | split_list

    count = compute(data_dict)
    count2 = compute_pt2(data_dict)
    print(f"Nb of bags can contain at least one shiny gold bag(part 1): {count}")

    print(f"Nb of bags in one shiny gold bag?(part 2): {count2}")


if __name__ == "__main__":
    main()
