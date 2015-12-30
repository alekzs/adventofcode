import re

def hasStraight(password):
    previous = None
    increasingStreak = 0
    completed = False
    for character in password:
        if previous and ord(character) - ord(previous) == 1:
            increasingStreak += 1
        else:
            increasingStreak = 0
        previous = character
        if increasingStreak == 2:
            completed = True
    return completed

def hasIol(password):
    return re.match(r'[iol]', password)

def hasTwoPairs(password):
    pairMatch = re.findall(r'(.)\1', password)
    return pairMatch and len(pairMatch) == 2

def increment(password):
    incrementedPass = ""
    wrappedAround = True
    for character in password[::-1]:
        if wrappedAround:
            nextChar = chr(ord(character) + 1)
            if ord(nextChar) > 122:
                nextChar = 'a'
                wrappedAround = True
            else:
                wrappedAround = False
        else:
            nextChar = character
        incrementedPass += nextChar
    return incrementedPass[::-1]

def solve(password):
    isValid = False
    while not isValid:
        password = increment(password)
        isValid = hasStraight(password) and not hasIol(password) and hasTwoPairs(password)
    print password

input = "hxbxwxba"
solve(input)
