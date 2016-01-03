import re
import itertools
from operator import mul

def solve(packages):
    compartmentWeight = sum(packages) / 4
    for i in range(len(packages)):
        combos = itertools.combinations(packages, i)
        fittingQe = [reduce(mul, c) for c in combos if sum(c) == compartmentWeight]
        if fittingQe:
            return min(fittingQe)

input = [
    1,
    3,
    5,
    11,
    13,
    17,
    19,
    23,
    29,
    31,
    37,
    41,
    43,
    47,
    53,
    59,
    67,
    71,
    73,
    79,
    83,
    89,
    97,
    101,
    103,
    107,
    109,
    113
]

print solve(input)
