import re
import itertools

def generateState(input):
    state = {}
    for deer in input:
        deerName, can, fly, speed, kms, forr, flightDuration, seconds, but, then, must, rest, forrr, restDuration, seconds2 = deer.split(" ")
        state[deerName] = {
            "speed": int(speed),
            "duration": int(flightDuration),
            "durationLeft": int(flightDuration),
            "rest": int(restDuration),
            "restLeft": int(restDuration),
            "distanceTravelled": 0
        }
    return state

def solve(input):
    state = generateState(input)
    for i in range(2505):
        for deerName in state:
            deer = state[deerName]
            if deer["durationLeft"] > 0:
                deer["distanceTravelled"] += deer["speed"]
                deer["durationLeft"] -= 1
                continue
            if deer["durationLeft"] == 0:
                if deer["restLeft"] > 0:
                   deer["restLeft"] -= 1
            if deer["restLeft"] == 0 and deer["durationLeft"] == 0:
                deer["restLeft"] = deer["rest"]
                deer["durationLeft"] = deer["duration"]
    print max(list(map(lambda (k, v): v["distanceTravelled"], state.iteritems())))
input = [
    "Dancer can fly 27 km/s for 5 seconds, but then must rest for 132 seconds.",
    "Cupid can fly 22 km/s for 2 seconds, but then must rest for 41 seconds.",
    "Rudolph can fly 11 km/s for 5 seconds, but then must rest for 48 seconds.",
    "Donner can fly 28 km/s for 5 seconds, but then must rest for 134 seconds.",
    "Dasher can fly 4 km/s for 16 seconds, but then must rest for 55 seconds.",
    "Blitzen can fly 14 km/s for 3 seconds, but then must rest for 38 seconds.",
    "Prancer can fly 3 km/s for 21 seconds, but then must rest for 40 seconds.",
    "Comet can fly 18 km/s for 6 seconds, but then must rest for 103 seconds.",
    "Vixen can fly 18 km/s for 5 seconds, but then must rest for 84 seconds."
]
solve(input)
