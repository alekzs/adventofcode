import re
import itertools

# Borrowed from https://www.reddit.com/r/adventofcode/comments/3xxdxt/day_23_solutions/cy8pi4d
def solve(commands):
    state = {'a': 1, 'b': 0}
    i = 0
    while True:
        if i not in range(len(commands)):
            break
        di = 1
        command, register = commands[i].split(" ", 1)
        if command == "hlf":
            state[register] //= 2
        elif command == "tpl":
            state[register] *= 3
        elif command == "inc":
            state[register] += 1
        elif command == "jmp":
            di = int(register)
        elif command == "jie":
            register, offset = register.split(',')
            if state[register] % 2 == 0:
                di = int(offset)
        elif command == "jio":
            register, offset = register.split(',')
            if state[register] == 1:
                di = int(offset)
        i += di
    print state["b"]

input = [
    "jio a, +16",
    "inc a",
    "inc a",
    "tpl a",
    "tpl a",
    "tpl a",
    "inc a",
    "inc a",
    "tpl a",
    "inc a",
    "inc a",
    "tpl a",
    "tpl a",
    "tpl a",
    "inc a",
    "jmp +23",
    "tpl a",
    "inc a",
    "inc a",
    "tpl a",
    "inc a",
    "inc a",
    "tpl a",
    "tpl a",
    "inc a",
    "inc a",
    "tpl a",
    "inc a",
    "tpl a",
    "inc a",
    "tpl a",
    "inc a",
    "inc a",
    "tpl a",
    "inc a",
    "tpl a",
    "tpl a",
    "inc a",
    "jio a, +8",
    "inc b",
    "jie a, +4",
    "tpl a",
    "inc a",
    "jmp +2",
    "hlf a",
    "jmp -7"
]

solve(input)
