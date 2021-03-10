import click

# 2 valid passports in this example
test_data = """ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in"""

# ignoring cid field
req_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]


def test_returns_right_number_of_valid_passport():
    assert compute(test_data) == 2


def test_spit_passports():
    nb_passports = 0

    list_of_passports = split_passports(test_data)
    nb_passports = len(list_of_passports)

    assert nb_passports == 4


def get_input_data_list_from_file(filename: str) -> str:
    with open(filename) as f:
        return f.read()


def split_passports(data: str) -> list:
    return data.split("\n\n")


def get_passport_fields(list_of_passport_fields: str) -> dict:
    return {field.split(":")[0]: field.split(":")[1] for field in list_of_passport_fields.split()}


def validate(passport: dict, req_keys: list) -> bool:
    is_valid = True

    for key in req_keys:
        if key not in passport.keys():
            is_valid = False
            break

    return is_valid


def compute(data: str) -> int:
    list_of_passports = split_passports(data)
    passport_dicts = []

    # change into dictionaries
    for passport in list_of_passports:
        passport_dicts.append(get_passport_fields(passport))

    count = 0
    for passport in passport_dicts:
        if validate(passport, req_fields):
            count += 1

    return count


@click.command()
@click.argument("filename")
def main(filename):
    input_data = get_input_data_list_from_file(filename)

    count = compute(input_data)
    print(f"Nb of valid passwords (part 1): {count}")


if __name__ == "__main__":
    main()
