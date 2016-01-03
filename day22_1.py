import re
import itertools
import random

spells = [
    # name, mana, damage, duration, increaseHp, increaseMana, increaseArmor
    ["Magic Missile", 53, 4, 0, 0, 0, 0],
    ["Drain", 73, 2, 0, 2, 0, 0],
    ["Shield", 113, 0, 6, 0, 0, 7],
    ["Poison", 173, 3, 6, 0, 0, 0],
    ["Recharge", 229, 0, 5, 0, 101, 0]
]

def simulate(bossHp, bossDamage):
    hp = 50
    mana = 500
    currentBossHp = bossHp
    myTurn = True
    won = False
    armor = 0
    activeEffects = {}

    spell = random.choice(spells)
    manaCost = 0
    while hp > 0 and mana > 0:
        #if myTurn:
        #    hp -= 1
        #apply active effects
        toRemove = []
        for effect in activeEffects:
            effectValue = activeEffects[effect]
            effectValue[3] = effectValue[3] - 1
            #print "%s duration decreased to %s" % (effect, effectValue[3])
            if effectValue[2]:
                #print "%s deals %s damage to boss" % (effect, effectValue[2])
                currentBossHp -= effectValue[2] if effectValue[2] > 0 else 1
            if effectValue[4]:
                #print "%s increases player hp by %s" % (effect, effectValue[4])
                hp += effectValue[4]
            if effectValue[5]:
                #print "%s increases player mana by %s" % (effect, effectValue[5])
                mana += effectValue[5]
            if effectValue[6]:
                #print "%s sets player armor to %s" % (effect, effectValue[6])
                armor = effectValue[6]
            if effectValue[3] == 0:
                #print "%s timer reaches 0" % effect
                toRemove.append(effect)
                if effectValue[6]:
                    armor = 0
        for effect in toRemove:
            activeEffects.pop(effect, None)
        if myTurn:
            spell = random.choice(spells)
            if activeEffects.get(spell[0]):
                while activeEffects.get(spell[0]):
                    spell = random.choice(spells)
            if mana - spell[1] < 0 and mana > 53:
                spell = spells[0]
            #print "player casts", spell
            if spell[3]:
                activeEffects[spell[0]] = list(spell)
            else:
                hit = spell[2]
                currentBossHp -= hit if hit > 0 else 1
                if spell[4]:
                    hp += spell[4]
                    #print "player health increased by %s" % spell[4]
                #print "player deals %s damage, boss hp: %s" % (hit, currentBossHp)
            manaCost += spell[1]
            mana -= spell[1]
        else:
            hit = bossDamage - armor
            hp -= hit if hit > 0 else 1
            #print "boss deals %s damage, player hp: %s" % (hit, hp)
        #print "-----------"
        if currentBossHp <= 0:
            won = True
            break
        myTurn = not myTurn
    return won, manaCost

def solve(bossHp, bossDamage):
    winningManas = []
    for i in range(10000):
        won, winningMana = simulate(bossHp, bossDamage)
        if won:
            winningManas.append(winningMana)
    print min(winningManas) if len(winningManas) else 0
solve(58, 9)
