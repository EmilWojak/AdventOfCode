from string import hexdigits, digits as decdigits
from typing import Callable, Dict, Iterable, TextIO, Tuple, cast


def is_valid_passport(passport: Dict[str, str]) -> bool:
    return all(
        field in passport.keys()
        for field in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    )


def is_valid_passport_strict(passport: Dict[str, str]) -> bool:
    rules = {
        "byr": lambda x: 1920 <= int(x) <= 2002,
        "iyr": lambda x: 2010 <= int(x) <= 2020,
        "eyr": lambda x: 2020 <= int(x) <= 2030,
        "hgt": lambda x: {
            "cm": lambda cm: 150 <= cm <= 193,
            "in": lambda inch: 59 <= inch <= 76,
        }[x[-2:]](int(x[:-2])),
        "hcl": lambda x: len(x) == 7
        and x[0] == "#"
        and all(digit in hexdigits.lower() for digit in x[1:]),
        "ecl": lambda x: x in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth"),
        "pid": lambda x: len(x) == 9 and all(digit in decdigits for digit in x),
    }
    try:
        return all(rule(passport[field]) for field, rule in rules.items())
    except KeyError:
        return False


def extract_passports_from_file(file: TextIO) -> Iterable[Dict[str, str]]:
    for passport in file.read().split("\n\n"):
        yield dict(
            cast(Tuple[str, str], field.split(":")) for field in passport.split()
        )


def count_valid_passports_in_file(
    file: TextIO, check_function: Callable[[Dict[str, str]], bool]
):
    return sum(
        check_function(passport) for passport in extract_passports_from_file(file)
    )


with open("d4.txt") as file:
    print(count_valid_passports_in_file(file, is_valid_passport))

with open("d4.txt") as file:
    print(count_valid_passports_in_file(file, is_valid_passport_strict))
