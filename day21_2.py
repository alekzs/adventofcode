import re
import itertools

# Name Cost  Damage  Armor
weapons = [
    "Dagger 8 4 0",
    "Shortsword 10 5 0",
    "Warhammer 25 6 0",
    "Longsword 40 7 0",
    "Greataxe 74 8 0"
]

armor = [
    "Leather 13 0 1",
    "Chainmail 31 0 2",
    "Splintmail 53 0 3",
    "Bandedmail 75 0 4",
    "Platemail 102 0 5"
]

rings = [
    "Damage+1 25 1 0",
    "Damage+2 50 2 0",
    "Damage+3 100 3 0",
    "Defense+1 20 0 1",
    "Defense+2 40 0 2",
    "Defense+3 80 0 3"
]

def simulate(damage, armor, bossHp, bossDamage, bossArmor):
    hp = 100
    currentBossHp = bossHp
    myTurn = True
    won = False
    while hp > 0 :
        if myTurn:
            hit = damage - bossArmor
            currentBossHp -= hit if hit > 0 else 1
        else:
            hit = bossDamage - armor
            hp -= hit if hit > 0 else 1
        if currentBossHp <= 0:
            won = True
            break
        myTurn = not myTurn
    return won

def evaluate(partialSet):
    totalCost = 0
    totalDamage = 0
    totalArmor = 0
    for item in partialSet:
        name, cost, damage, armor = item.split(" ")
        totalCost += int(cost)
        totalDamage += int(damage)
        totalArmor += int(armor)
    return (totalCost, totalDamage, totalArmor)

def solve(bossHp, bossDamage, bossArmor):
    pricesThatLost = []
    for combo in list(itertools.product(weapons, armor, rings, rings)):
        fullSet = list(combo)
        combos = []
        for i in range(len(fullSet[1:])):
            combos.append(list(itertools.combinations(fullSet[1:], i)))
        combos.append([tuple(fullSet[1:])])
        for combinationSet in combos:
            for combination in combinationSet:
                partialSet = list(set([fullSet[0]] + list(combination)))
                setPrice, setDamage, setArmor = evaluate(partialSet)
                if not simulate(setDamage, setArmor, bossHp, bossDamage, bossArmor):
                    pricesThatLost.append(setPrice)
    print max(pricesThatLost) if len(pricesThatLost) else 0

solve(109, 8, 2)
