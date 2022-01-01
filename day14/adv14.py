#!/usr/bin/env python3

import sys
from typing import Dict, List, Tuple

def extend_polymer(polymer: str, polymer_extention: Dict[str, str]) -> str:
    extended = ''
    for pair in zip(polymer, polymer[1:]):
        pair_str = ''.join(pair)
        extended += polymer_extention[pair_str]
    return extended + polymer[-1]


def get_element_comp(polymer: str) -> Dict[str, int]:
    element_comp = {}
    for elem in polymer:
        if elem not in element_comp.keys():
            element_comp[elem] = 1
        else:
            element_comp[elem] += 1
    return element_comp


def get_maxmin(element_comp: Dict[str, int]) -> Tuple[int, int]:
    max_elem = 0
    min_elem = sys.maxsize
    for element in element_comp:
        max_elem = max(element_comp[element], max_elem)
        min_elem = min(element_comp[element], min_elem)
    return max_elem, min_elem


def get_polymer_diff(polymer_template: str, polymer_extention: Dict[str, str], loops: int) -> int:
    polymer = polymer_template[:]
    for i in range(loops):
        polymer = extend_polymer(polymer, polymer_extention)
    element_comp = get_element_comp(polymer)
    max_elem, min_elem = get_maxmin(element_comp)
    return max_elem - min_elem


def adv14_1(polymer_template: str, polymer_extentions: Dict[str, str]) -> int:
    return get_polymer_diff(polymer_template, polymer_extentions, 10)


def p2(polymer_template: str, polymer_extentions: Dict[str, str]) -> int:
    polymer_pairs: Dict[str, int] = {}
    for pair in zip(polymer_template, polymer_template[1:]):
        pair_str = ''.join(pair)
        polymer_pairs[pair_str] = 1

    for i in range(40):
        temp_pairs: Dict[str, int] = {}
        for pair in polymer_pairs:
            if polymer_pairs[pair] > 0:
                count = polymer_pairs[pair]
                polymer_pairs[pair] = 0
                extend = polymer_extentions[pair]
                if extend not in temp_pairs.keys():
                    temp_pairs[extend] = count
                else:
                    temp_pairs[extend] += count
        polymer_pairs = temp_pairs
    print(polymer_pairs)

def adv14_2(polymer_template: str, polymer_extentions: Dict[str, str]) -> int:
    # return get_polymer_diff(polymer_template, polymer_extentions, 40)
    return p2(polymer_template, polymer_extentions)



def construct_polymer_extentions(polymer_data: List[str]) -> Dict[str, str]:
    extentions: Dict[str, str] = {}
    for line in polymer_data:
        polymer_base = line.strip().split()
        extentions[polymer_base[0]] = polymer_base[0][:1] + polymer_base[2]
    return extentions


def main():
    data = []
    with open("polymer_data.txt") as f:
        data = f.readlines()
    f.close

    polymer_template: str = data[0].strip()
    polymer_extention: Dict[str, str] = construct_polymer_extentions(data[2:])

    print("part 1 - Polymer value after 10 iterations:", adv14_1(polymer_template, polymer_extention))
    print("part 2 - Polymer value after 40 iterations:", adv14_2(polymer_template, polymer_extention))

if __name__ == '__main__':
    main()
