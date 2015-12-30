import re
import itertools
maxLiters = 150
def calculateCombinations(allCombinations, shouldCalculateMinContainers, minContainersInput):
    correctCombinations = 0
    differentWays = 0
    minContainers = len(allCombinations)
    maxLiters = 150

    for combinationGroup in allCombinations:
        for combination in combinationGroup:
            if sum(list(combination)) == maxLiters:
                minContainers = min(minContainers, len(list(combination)))
                if minContainersInput and len(list(combination)) == minContainersInput:
                    differentWays += 1
                correctCombinations += 1
    if shouldCalculateMinContainers:
        return minContainers
    return differentWays

def solve(input):
    containers = input
    allCombinations = []
    for i in range(1, len(containers)):
        allCombinations.append(list(itertools.combinations(containers, i)))

    minContainers = calculateCombinations(allCombinations, True, 0)
    print calculateCombinations(allCombinations, False, minContainers)

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
