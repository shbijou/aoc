import pytest
import click
import re


# 4 valid passports in this example
test_data = """eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007

pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719"""

# ignoring cid field
req_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

valid_ecl = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]


@pytest.mark.parametrize("test_input,expected", [("2002", True), ("2003", False)])
def test_validate_byr(test_input, expected):
    assert validate_byr(test_input) == expected


@pytest.mark.parametrize("test_input,expected", [("60in", True), ("190cm", True), ("190in", False), ("190", False)])
def test_validate_hgt(test_input, expected):
    assert validate_hgt(test_input) == expected


@pytest.mark.parametrize("test_input,expected", [("#123abc", True), ("#123abz", False), ("123abc", False)])
def test_validate_hcl(test_input, expected):
    assert validate_hcl(test_input) == expected


@pytest.mark.parametrize("test_input,expected", [("brn", True), ("wat", False)])
def test_validate_ecl(test_input, expected):
    assert validate_ecl(test_input) == expected


@pytest.mark.parametrize("test_input,expected", [("000000001", True), ("0123456789", False)])
def test_validate_pid(test_input, expected):
    assert validate_pid(test_input) == expected


def test_returns_right_number_of_valid_passport():
    assert compute(test_data) == 8
    assert compute_pt2(test_data) == 4


def test_spit_passports():
    nb_passports = 0

    list_of_passports = split_passports(test_data)
    nb_passports = len(list_of_passports)

    assert nb_passports == 8


def get_input_data_list_from_file(filename: str) -> str:
    with open(filename) as f:
        return f.read()


def split_passports(data: str) -> list:
    return data.split("\n\n")


def get_passport_fields(list_of_passport_fields: str) -> dict:
    return {field.split(":")[0]: field.split(":")[1] for field in list_of_passport_fields.split()}


def validate_byr(value: str) -> bool:
    return len(value) == 4 and 1920 <= int(value) <= 2002


def validate_iyr(value: str) -> bool:
    return len(value) == 4 and 2010 <= int(value) <= 2020


def validate_eyr(value: str) -> bool:
    return len(value) == 4 and 2020 <= int(value) <= 2030


def validate_hgt(value: str) -> bool:
    is_valid = False

    pattern_matches = list(filter(None, re.split("(\d+)(in|cm)", value)))
    if len(pattern_matches) > 1:
        val, unit = pattern_matches
        if unit == "cm":
            if 150 <= int(val) <= 193:
                is_valid = True
        if unit == "in":
            if 59 <= int(val) <= 76:
                is_valid = True

    return is_valid


def validate_hcl(value: str) -> bool:
    return re.match("#[0-9a-f]{6}", value) is not None


def validate_ecl(value: str) -> bool:
    return value in valid_ecl


def validate_pid(value: str) -> bool:
    return len(value) == 9 and value.isnumeric()


def validate_data(key: str, value: str) -> bool:
    if key == "byr":
        is_valid = validate_byr(value)
    if key == "iyr":
        is_valid = validate_iyr(value)
    if key == "eyr":
        is_valid = validate_eyr(value)
    if key == "hgt":
        is_valid = validate_hgt(value)
    if key == "hcl":
        is_valid = validate_hcl(value)
    if key == "ecl":
        is_valid = validate_ecl(value)
    if key == "pid":
        is_valid = validate_pid(value)

    return is_valid


def validate_and_check_data(passport: dict, req_keys: list) -> bool:
    is_valid = True

    for key in req_keys:
        if key not in passport.keys():
            is_valid = False
            break

        if validate_data(key, passport[key]) is False:
            is_valid = False
            break

    return is_valid


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


def compute_pt2(data: str) -> int:
    list_of_passports = split_passports(data)
    passport_dicts = []

    # change into dictionaries
    for passport in list_of_passports:
        passport_dicts.append(get_passport_fields(passport))

    count = 0
    for passport in passport_dicts:
        if validate_and_check_data(passport, req_fields):
            count += 1

    return count


@click.command()
@click.argument("filename")
def main(filename):
    input_data = get_input_data_list_from_file(filename)

    count = compute(input_data)
    print(f"Nb of valid passwords (part 1): {count}")

    print(f"Nb of valid passwords (part 2): {compute_pt2(input_data)}")


if __name__ == "__main__":
    main()
