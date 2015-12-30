import re

def solve(input):
    previous = None
    matchingCounter = 1
    output = ""
    input += " "
    for character in input:
        if previous and previous == character:
            matchingCounter += 1
        else:
            if previous:
                output += str(matchingCounter) + str(previous)
            matchingCounter = 1
        previous = character
    return output

input = "1113122113"
for i in range(50):
    input = solve(input)
print len(input)