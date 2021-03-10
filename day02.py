import click


def get_input_data_list_from_file(filename: str) -> list:
    with open(filename) as f:
        return f.read().splitlines()


@click.command()
@click.argument("filename")
def main(filename):

    input_data = get_input_data_list_from_file(filename)
    valid_password_count_part1 = 0
    valid_password_count_part2 = 0

    for k, v in enumerate(input_data):
        policy, password = v.split(":")

        min_max, char = policy.split(" ")

        min_occur, max_occur = list(map(int, min_max.split("-")))

        if password.count(char) >= min_occur and password.count(char) <= max_occur:
            valid_password_count_part1 += 1

        if password[min_occur] == char or password[max_occur] == char:
            if password[min_occur] == char and password[max_occur] == char:
                continue
            valid_password_count_part2 += 1

    print(f"Nb of valid passwords found (method1): {valid_password_count_part1}")
    print(f"Nb of valid passwords found (method2): {valid_password_count_part2}")


if __name__ == "__main__":
    main()
