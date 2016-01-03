import re
import itertools

def solve(input):
    distanceMap = {}
    for distance in input:
        distArray = distance.split(' = ')
        start = distArray[0].split(' to ')[0]
        end = distArray[0].split(' to ')[1]

        destination = {}
        if start in distanceMap:
            destination = distanceMap[start]
        destination[end] = int(distArray[1])
        distanceMap[start] = destination

        destinationEnd = {}
        if end in distanceMap:
            destinationEnd = distanceMap[end]
        destinationEnd[start] = int(distArray[1])
        distanceMap[end] = destinationEnd

    paths = []

    for permutation in list(itertools.permutations(distanceMap)):
        valid = False
        distance = 0
        permutation = list(permutation)
        for i in range(len(permutation) - 1):
            start = permutation[i]
            end = permutation[i + 1]
            if end in distanceMap[start]:
                distance += distanceMap[start][end]
            else:
                break
            if end == permutation[len(permutation) - 1] and end in distanceMap[start]:
                valid = True
        if valid:
            paths.append(distance)
    paths.sort()
    print list(reversed(paths))[0]

input = [
    "Faerun to Tristram = 65",
    "Faerun to Tambi = 129",
    "Faerun to Norrath = 144",
    "Faerun to Snowdin = 71",
    "Faerun to Straylight = 137",
    "Faerun to AlphaCentauri = 3",
    "Faerun to Arbre = 149",
    "Tristram to Tambi = 63",
    "Tristram to Norrath = 4",
    "Tristram to Snowdin = 105",
    "Tristram to Straylight = 125",
    "Tristram to AlphaCentauri = 55",
    "Tristram to Arbre = 14",
    "Tambi to Norrath = 68",
    "Tambi to Snowdin = 52",
    "Tambi to Straylight = 65",
    "Tambi to AlphaCentauri = 22",
    "Tambi to Arbre = 143",
    "Norrath to Snowdin = 8",
    "Norrath to Straylight = 23",
    "Norrath to AlphaCentauri = 136",
    "Norrath to Arbre = 115",
    "Snowdin to Straylight = 101",
    "Snowdin to AlphaCentauri = 84",
    "Snowdin to Arbre = 96",
    "Straylight to AlphaCentauri = 107",
    "Straylight to Arbre = 14",
    "AlphaCentauri to Arbre = 46"
]
solve(input)