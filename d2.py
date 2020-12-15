from typing import Iterable, cast
from parse import parse, Result


def count_valid_passwords_1(passwords: Iterable[str]) -> int:
    return sum(
        (od <= haslo.count(znak) <= do)
        for (od, do, znak, haslo) in (
            cast(Result, parse("{:d}-{:d} {}: {}", line)).fixed for line in passwords
        )
    )


def count_valid_passwords_2(passwords: Iterable[str]) -> int:
    return sum(
        (haslo[a - 1] == znak) ^ (haslo[b - 1] == znak)
        for a, b, znak, haslo in (
            cast(Result, parse("{:d}-{:d} {}: {}", line)).fixed for line in passwords
        )
    )


print(count_valid_passwords_1(open("d2.txt")))
print(count_valid_passwords_2(open("d2.txt")))
