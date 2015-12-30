import re
import itertools

def generateState(input):
    state = {}
    for ingredient in input:
        name, c, capacity, d, durability, f, flavor, t, texture, c, calories = ingredient.split(" ")
        name = name.replace(":", "")
        state[name] = {
            "capacity": int(capacity.replace(",", "")),
            "durability": int(durability.replace(",", "")),
            "flavor": int(flavor.replace(",", "")),
            "texture": int(texture.replace(",", "")),
            "calories": int(calories.replace(",", ""))
        }
    return state

def solve(input):
    state = generateState(input)
    scores = []
    for a in range(100):
        for b in range(100 - a):
            for c in range(100 - a - b):
                 d = 100 - a - b - c
                 scoreCapacity = a * state["Sprinkles"]["capacity"] + b * state["Butterscotch"]["capacity"] + c * state["Chocolate"]["capacity"] + d * state["Candy"]["capacity"]
                 scoreDurability = a * state["Sprinkles"]["durability"] + b * state["Butterscotch"]["durability"] + c * state["Chocolate"]["durability"] + d * state["Candy"]["durability"]
                 scoreFlavor = a * state["Sprinkles"]["flavor"] + b * state["Butterscotch"]["flavor"] + c * state["Chocolate"]["flavor"] + d * state["Candy"]["flavor"]
                 scoreTexture = a * state["Sprinkles"]["texture"] + b * state["Butterscotch"]["texture"] + c * state["Chocolate"]["texture"] + d * state["Candy"]["texture"]
                 calories = a * state["Sprinkles"]["calories"] + b * state["Butterscotch"]["calories"] + c * state["Chocolate"]["calories"] + d * state["Candy"]["calories"]
                 #print a, b, c, d, "|", scoreCapacity, scoreDurability, scoreFlavor, scoreTexture, scoreCapacity * scoreDurability  * scoreFlavor * scoreTexture
                 if calories == 500:
                    scores.append(max(scoreCapacity, 0) * max(scoreDurability, 0)  * max(scoreFlavor, 0) * max(scoreTexture, 0))

    print max(scores)
input = [
    "Sprinkles: capacity 2, durability 0, flavor -2, texture 0, calories 3",
    "Butterscotch: capacity 0, durability 5, flavor -3, texture 0, calories 3",
    "Chocolate: capacity 0, durability 0, flavor 5, texture -1, calories 8",
    "Candy: capacity 0, durability -1, flavor 0, texture 5, calories 8"
]
solve(input)
