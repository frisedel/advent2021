#!/usr/bin/env python3

import sys
from typing import Dict, List

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


def get_maxmin(element_comp: Dict[str, int]):
    max_elem = 0
    min_elem = sys.maxsize

    for element in element_comp:
        max_elem = max(element_comp[element], max_elem)
        min_elem = min(element_comp[element], min_elem)

    return max_elem, min_elem


def adv14_1(polymer_template: str, polymer_extention: Dict[str, str]) -> int:
    polymer = polymer_template[:]
    for i in range(10):
        polymer = extend_polymer(polymer, polymer_extention)

    element_comp = get_element_comp(polymer)
    max_elem, min_elem = get_maxmin(element_comp)

    return max_elem - min_elem


def adv14_2():
    pass


def construct_polymer_extentions(polymer_data: List[str]):
    extention: Dict[str, str] = {}
    for line in polymer_data:
        polymer_base = line.strip().split()
        extention[polymer_base[0]] = polymer_base[0][:1] + polymer_base[2]
    return extention


def main():
    data = []
    with open("polymer_data.txt") as f:
        data = f.readlines()
    f.close

    polymer_template: str = data[0].strip()

    polymer_extention: Dict[str, str] = construct_polymer_extentions(data[2:])

    print("part 1 - :", adv14_1(polymer_template, polymer_extention))
    print("part 2 - :", adv14_2())

if __name__ == '__main__':
    main()
