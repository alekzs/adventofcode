import re
import itertools

def find(source, substring):
    return [m.start() for m in re.finditer(substring, source)]

def solve(replacements, molecule):
    moleculeCombinations = []
    for replacement in replacements:
        replacementFrom = replacement.split(" => ")[0]
        replacementTo = replacement.split(" => ")[1]
        locations = find(molecule, replacementFrom)
        for replacementIndex in locations:
            newMolecule = molecule[:replacementIndex] + replacementTo + molecule[replacementIndex + len(replacementFrom):]
            if not newMolecule in moleculeCombinations:
                moleculeCombinations.append(newMolecule)
    print len(moleculeCombinations)

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
    "O => HH"
]

testMolecule = "HOH"

molecule = "ORnPBPMgArCaCaCaSiThCaCaSiThCaCaPBSiRnFArRnFArCaCaSiThCaCaSiThCaCaCaCaCaCaSiRnFYFArSiRnMgArCaSiRnPTiTiBFYPBFArSiRnCaSiRnTiRnFArSiAlArPTiBPTiRnCaSiAlArCaPTiTiBPMgYFArPTiRnFArSiRnCaCaFArRnCaFArCaSiRnSiRnMgArFYCaSiRnMgArCaCaSiThPRnFArPBCaSiRnMgArCaCaSiThCaSiRnTiMgArFArSiThSiThCaCaSiRnMgArCaCaSiRnFArTiBPTiRnCaSiAlArCaPTiRnFArPBPBCaCaSiThCaPBSiThPRnFArSiThCaSiThCaSiThCaPTiBSiRnFYFArCaCaPRnFArPBCaCaPBSiRnTiRnFArCaPRnFArSiRnCaCaCaSiThCaRnCaFArYCaSiRnFArBCaCaCaSiThFArPBFArCaSiRnFArRnCaCaCaFArSiRnFArTiRnPMgArF"

solve(input, molecule)
#solve(testInput, testMolecule)
