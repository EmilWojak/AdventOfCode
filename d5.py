from functools import reduce
from itertools import islice
from typing import Iterable


def seat_to_id(seat: str) -> int:
    return reduce(lambda x, y: 2 * x + y, (int(c in "BR") for c in seat))


def find_missing_seat(seats: Iterable[int]) -> int:
    seats = sorted(seats)
    return next(
        prev + 1
        for (prev, next) in zip(seats, islice(seats, 1, None))
        if next - prev == 2
    )


with open("d5.txt") as file:
    seats = [seat_to_id(seat) for seat in (line.strip() for line in file)]
    print(reduce(max, seats))
    print(find_missing_seat(seats))