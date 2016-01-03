import re
import itertools
import random

def solve(replacements, molecule):
    state = []
    visited = []

    for replacement in replacements:
        replacementFrom = replacement.split(" => ")[0]
        replacementTo = replacement.split(" => ")[1]
        state.append((replacementFrom, replacementTo))


    random.shuffle(state)
    #state = sorted(state, key=lambda x: -len(x[1]))
    print state
    target = molecule
    steps = 0
    while target != "e":
        tempMolecule = target
        for src, replacement in state:
            if replacement in target:
                target = target.replace(replacement, src, 1)
                steps += 1
        if tempMolecule == target:
            target = molecule
            steps = 0
            random.shuffle(state)

    print steps

input = [
    "Al => ThF",
    "Al => ThRnFAr",
    "B => BCa",
    "B => TiB",
    "B => TiRnFAr",
    "Ca => CaCa",
    "Ca => PB",
    "Ca => PRnFAr",
    "Ca => SiRnFYFAr",
    "Ca => SiRnMgAr",
    "Ca => SiTh",
    "F => CaF",
    "F => PMg",
    "F => SiAl",
    "H => CRnAlAr",
    "H => CRnFYFYFAr",
    "H => CRnFYMgAr",
    "H => CRnMgYFAr",
    "H => HCa",
    "H => NRnFYFAr",
    "H => NRnMgAr",
    "H => NTh",
    "H => OB",
    "H => ORnFAr",
    "Mg => BF",
    "Mg => TiMg",
    "N => CRnFAr",
    "N => HSi",
    "O => CRnFYFAr",
    "O => CRnMgAr",
    "O => HP",
    "O => NRnFAr",
    "O => OTi",
    "P => CaP",
    "P => PTi",
    "P => SiRnFAr",
    "Si => CaSi",
    "Th => ThCa",
    "Ti => BP",
    "Ti => TiTi",
    "e => HF",
    "e => NAl",
    "e => OMg"
]

testInput = [
    "H => HO",
    "H => OH",
    "O => HH",
    "e => H",
    "e => O"
]

testMolecule = "HOHOHO"

molec = "ORnPBPMgArCaCaCaSiThCaCaSiThCaCaPBSiRnFArRnFArCaCaSiThCaCaSiThCaCaCaCaCaCaSiRnFYFArSiRnMgArCaSiRnPTiTiBFYPBFArSiRnCaSiRnTiRnFArSiAlArPTiBPTiRnCaSiAlArCaPTiTiBPMgYFArPTiRnFArSiRnCaCaFArRnCaFArCaSiRnSiRnMgArFYCaSiRnMgArCaCaSiThPRnFArPBCaSiRnMgArCaCaSiThCaSiRnTiMgArFArSiThSiThCaCaSiRnMgArCaCaSiRnFArTiBPTiRnCaSiAlArCaPTiRnFArPBPBCaCaSiThCaPBSiThPRnFArSiThCaSiThCaSiThCaPTiBSiRnFYFArCaCaPRnFArPBCaCaPBSiRnTiRnFArCaPRnFArSiRnCaCaCaSiThCaRnCaFArYCaSiRnFArBCaCaCaSiThFArPBFArCaSiRnFArRnCaCaCaFArSiRnFArTiRnPMgArF"

solve(input, molec)
#solve(testInput, testMolecule)
