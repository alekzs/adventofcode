import re
import itertools

def solve(input):
    maxLiters = 150
    containers = input
    allCombinations = []
    correctCombinations = 0
    for i in range(1, len(containers)):
        allCombinations.append(list(itertools.combinations(containers, i)))

    for combinationGroup in allCombinations:
        for combination in combinationGroup:
            if sum(list(combination)) == maxLiters:
                correctCombinations += 1
    print correctCombinations

input = [
    33,
    14,
    18,
    20,
    45,
    35,
    16,
    35,
    1,
    13,
    18,
    13,
    50,
    44,
    48,
    6,
    24,
    41,
    30,
    42
]

solve(input)
