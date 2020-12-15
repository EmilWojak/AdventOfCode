from typing import Iterable
from functools import reduce
from operator import mul


def count_trees(lines: Iterable[str], right: int, down: int):
    trees = 0
    position = 0
    for n, line in enumerate(lines):
        if n % down == 0:
            trees += line[position] == "#"
            position += right
            position %= len(line)
    return trees


with open("d3.txt") as file:
    lines = [line.strip() for line in file]

tree_counts = (
    count_trees(lines, right, down)
    for (right, down) in ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))
)

print(reduce(mul, tree_counts))
