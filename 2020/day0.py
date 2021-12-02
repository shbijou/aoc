import pytest
import click
import re
from typing import List, Optional, Dict, Any
from copy import copy

test_data = None


def get_input_data_list_from_file(filename: str) -> str:
    with open(filename) as f:
        return f.read()


@click.command()
@click.argument("filename")
def main(filename):
    input_data = get_input_data_list_from_file(filename)

    count = 0

    print(f"(part 1): {count}")
    print(f"(part 2): {count}")


if __name__ == "__main__":
    main()
