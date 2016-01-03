import re
import itertools
from operator import mul

def solve(code):
    print "Final day, ho ho ho!"
    targetRow = int(re.findall(r'\d+', code)[0])
    targetCol = int(re.findall(r'\d+', code)[1])
    currentNum = 20151125
    for i in range(1, 10000): #3011
        for j in range(1, i + 1):
            calcRow = i - j + 1
            calcCol = j
            if calcRow == targetRow and calcCol == targetCol:
                return currentNum
            currentNum = (currentNum * 252533) % 33554393

input = "To continue, please consult the code grid in the manual.  Enter the code at row 3010, column 3019."
print solve(input)
