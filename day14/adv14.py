#!/usr/bin/env python3

import sys
from typing import Counter, Dict, List, Tuple
from copy import deepcopy

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


def p2(pairs: Dict[str, int], polymer_extentions: Dict[str, str]) -> int:
    polymer = deepcopy(pairs)
    for i in range(40):
        new_pairs = {}
        for pair in polymer:
            extend = polymer_extentions[pair]
            first_pair = pair[0] + extend
            second_pair = extend + pair[1]
            if first_pair not in new_pairs.keys():
                new_pairs[first_pair] = polymer[pair]
            else:
                new_pairs[first_pair] += polymer[pair]
            if second_pair not in new_pairs.keys():
                new_pairs[second_pair] = polymer[pair]
            else:
                new_pairs[second_pair] += polymer[pair]
        polymer = deepcopy(new_pairs)
    return polymer

def adv14_2(polymer_template: str, polymer_data: List[str]) -> int:
    first_pairs = {}
    for pair in zip(polymer_template, polymer_template[1:]):
        pair_str = ''.join(pair)
        if pair_str not in first_pairs.keys():
           first_pairs[pair_str] = 1
        else:
            first_pairs[pair_str] += 1

    polymer_extentions = {}
    for line in polymer_data:
        polymer_base = line.strip().split()
        polymer_extentions[polymer_base[0]] = polymer_base[2]
        
    polymer = p2(first_pairs, polymer_extentions)

    counted = {}
    for pair in polymer:
        if pair[0] not in counted.keys():
            counted[pair[0]] = polymer[pair]
        else:
            counted[pair[0]] += polymer[pair]
        if pair[1] not in counted.keys():
            counted[pair[1]] = polymer[pair]
        else:
            counted[pair[1]] += polymer[pair]
    counted[polymer_template[-1]] += 1
    max_pol, min_pol = get_maxmin(counted)
    return max_pol-min_pol


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

    #print("part 1 - Polymer value after 10 iterations:", adv14_1(polymer_template, polymer_extention))
    print("part 2 - Polymer value after 40 iterations:", adv14_2(polymer_template, data[2:]))

if __name__ == '__main__':
    main()