import re
import itertools

def factors(n):
    return list(set(reduce(list.__add__,
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))))

def numPresentsForHouse(houseNumber):
    return sum([x * 10 for x in factors(houseNumber)])

def solve(presents):
    numPresents = 0
    houseNumber = 0
    while numPresents < presents:
        houseNumber += 1
        numPresents = numPresentsForHouse(houseNumber)

    print houseNumber


input = 33100000

solve(input)
