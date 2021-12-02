import pytest
import click
import re
from typing import Dict, List
from dataclasses import dataclass


test1_data = """abcx
abcy
abcz"""

test2_data = """abc

a
b
c

ab
ac

a
a
a
a

b"""


def get_input_data_list_from_file(filename: str) -> str:
    with open(filename) as f:
        return f.read()


@click.command()
@click.argument("filename")
def main(filename):
    input_data = get_input_data_list_from_file(filename)
    # input_data = test2_data

    count1 = 0
    count2 = 0

    groups = input_data.split("\n\n")
    new_groups = []

    for group in groups:
        questions = {}
        new_groups.append(group.splitlines())
        group = group.replace("\n", "")
        for answer in group:
            if answer in questions.keys():
                questions[answer] += 1
            else:
                questions.update({answer: 1})
        count1 += len(questions.keys())

    for group in new_groups:
        new_questions = {}
        for person in group:
            nb_of_persons = len(group)
            for answer in person:
                if answer in new_questions.keys():
                    new_questions[answer] += 1
                else:
                    new_questions.update({answer: 1})

        tab = []
        for key in new_questions.keys():
            if new_questions[key] == nb_of_persons:
                tab.append(key)
        count2 += len(list(dict.fromkeys(tab)))

    print(f'questions to which ANYONE answered "yes". (PART 1): {count1}')
    print(f'questions to which EVERYONE answered "yes". (PART 2): {count2}')


if __name__ == "__main__":
    main()
