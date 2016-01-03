import hashlib
secret = "yzbqklnj"
number = 0
current = secret
has5LeadingZeroes = False
while not has5LeadingZeroes:
    number += 1
    current = secret + str(number)
    hexCurrent = hashlib.md5(current.encode()).hexdigest()
    if hexCurrent[:5] == "00000":
        has5LeadingZeroes = True

print number