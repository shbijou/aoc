import click
import requests
from copy import copy


def get_input_data_list_from_file(filename: str) -> list:
    with open(filename) as f:
        return list(map(int, f.read().splitlines()))


def compute(input_data):
    for i in range(len(input_data)):

        temp_list = copy(input_data)
        val1 = temp_list.pop(i)

        for j in range(len(temp_list)):

            temp_list2 = copy(temp_list)
            val2 = temp_list2.pop(j)

            for k in range(len(temp_list2)):

                val3 = temp_list2[k]

                if val1 + val2 + val3 == 2020:
                    return val1, val2, val3


@click.command()
@click.argument("filename")
def main(filename):
    # Need to login first
    # input_data = requests.get("https://adventofcode.com/2020/day/1/input").text

    input_data = get_input_data_list_from_file(filename)

    val1, val2, val3 = compute(input_data)

    print(f"{val1}+{val2}+{val3}={val1 + val2 + val3}")
    print(f"{val1}*{val2}*{val3}={val1 * val2 * val3}")


if __name__ == "__main__":
    # execute only if run as a script
    main()
