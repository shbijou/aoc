import click


def get_input_data_list_from_file(filename: str) -> list:
    with open(filename) as f:
        return f.read().splitlines()


def compute(input_data, right, down):
    line = 0
    col = 0
    trees = 0

    while line < len(input_data) - 1:
        line += down
        col += right

        if col >= len(input_data[line]):
            col = col - len(input_data[line])
        if input_data[line][col] == "#":
            trees += 1

    return trees


@click.command()
@click.argument("filename")
def main(filename):
    input_data = get_input_data_list_from_file(filename)
    trees = 0

    trees = compute(input_data, 3, 1)
    print(f"Nb of trees (part 1): {trees}")

    trees *= compute(input_data, 1, 1)
    trees *= compute(input_data, 5, 1)
    trees *= compute(input_data, 7, 1)
    trees *= compute(input_data, 1, 2)
    print(f"Nb of trees (part 2): {trees}")


if __name__ == "__main__":
    main()
