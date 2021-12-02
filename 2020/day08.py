import pytest
import click
import re
from typing import List, Optional, Dict, Any
from copy import copy

test_data = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6"""


def get_input_data_list_from_file(filename: str) -> str:
    with open(filename) as f:
        return f.read()


def run_program(program: List[str]):
    # Registers
    exit_code = 0
    accum = 0
    prog_counter = 0
    loop_check = set()

    while prog_counter < len(program):
        operation, argument = program[prog_counter].split()
        argument = int(argument)

        # print(f"{operation} {argument}")
        # print(f"{prog_counter} {accum}")

        if operation == "acc":
            accum += argument
            prog_counter += 1

        if operation == "jmp":
            prog_counter += argument

        if operation == "nop":
            prog_counter += 1

        try:
            assert prog_counter not in loop_check

        except:
            exit_code = -1
            break
        loop_check.add(prog_counter)

    return exit_code, accum


@click.command()
@click.argument("filename")
def main(filename):
    input_data = get_input_data_list_from_file(filename)

    program = input_data.splitlines()
    # program = test_data.splitlines()

    exit_code, accum = run_program(program)

    print(f"value of the accumulator before loop(part 1): {accum}")

    jmp_nop_lines = list()
    exit_code = -1
    accum = 0

    for line_index in range(len(program)):
        if "jmp" in program[line_index] or "nop" in program[line_index]:
            jmp_nop_lines.append(line_index)

    while exit_code == -1:
        temp_program = copy(program)
        line_index = jmp_nop_lines.pop(0)

        if "jmp" in temp_program[line_index]:
            temp_program[line_index] = temp_program[line_index].replace("jmp", "nop")
        else:
            temp_program[line_index] = temp_program[line_index].replace("nop", "jmp")

        exit_code, accum = run_program(temp_program)

    print(f"value of the accumulator after normal exit(part 2): {accum}")


if __name__ == "__main__":
    main()
