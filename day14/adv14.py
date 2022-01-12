#!/usr/bin/env python3

from typing import Dict, List, Tuple
from copy import deepcopy

def extend_polymer_string(polymer: str, polymer_extention: Dict[str, str]) -> str:
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
    values = list(element_comp.values())
    return max(values), min(values)


def get_polymer_str_diff(polymer_template: str, polymer_extention: Dict[str, str], loops: int) -> int:
    polymer = polymer_template[:]
    for i in range(loops):
        polymer = extend_polymer_string(polymer, polymer_extention)
    element_comp = get_element_comp(polymer)
    max_elem, min_elem = get_maxmin(element_comp)
    return max_elem - min_elem


def adv14_1(polymer_template: str, polymer_extentions: Dict[str, str]) -> int:
    return get_polymer_str_diff(polymer_template, polymer_extentions, 10)


def process_polymer(pairs: Dict[str, int], polymer_extentions: Dict[str, str], iterations: int) -> Dict[str, int]:
    polymer = deepcopy(pairs)
    for i in range(iterations):
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


def calculate_first_pairs(polymer_template: str) -> Dict[str, int]:
    pairs: Dict[str, int] = {}
    for pair in zip(polymer_template, polymer_template[1:]):
        pair_str = ''.join(pair)
        if pair_str not in pairs.keys():
           pairs[pair_str] = 1
        else:
            pairs[pair_str] += 1
    return pairs


def count_elements(polymer: Dict[str, int], last_char: str):
    counted = {}
    for pair in polymer:
        if pair[0] not in counted.keys():
            counted[pair[0]] = polymer[pair]
        else:
            counted[pair[0]] += polymer[pair]
    counted[last_char] += 1
    return counted


def get_polymer_dict_diff(polymer_template: str, polymer_dict_extention: Dict[str, str], iterations: int):
    first_pairs = calculate_first_pairs(polymer_template)
    polymer = process_polymer(first_pairs, polymer_dict_extention, iterations)
    counted = count_elements(polymer, polymer_template[-1])

    polymer_max, polymer_min = get_maxmin(counted)
    return polymer_max - polymer_min


def adv14_2(polymer_template: str, polymer_dict_extention: Dict[str, str]) -> int:
    return get_polymer_dict_diff(polymer_template, polymer_dict_extention, 40)


def construct_polymer_str_extentions(polymer_data: List[str]) -> Dict[str, str]:
    extentions: Dict[str, str] = {}
    for line in polymer_data:
        polymer_base = line.strip().split()
        extentions[polymer_base[0]] = polymer_base[0][:1] + polymer_base[2]
    return extentions


def construct_polymer_dict_extentions(polymer_data: List[str]) -> Dict[str, str]:
    polymer_extentions: Dict[str, str] = {}
    for line in polymer_data:
        polymer_base = line.strip().split()
        polymer_extentions[polymer_base[0]] = polymer_base[2]
    return polymer_extentions


def main():
    data = []
    with open("polymer_data.txt") as f:
        data = f.readlines()
    f.close

    polymer_template: str = data[0].strip()
    polymer_str_extention: Dict[str, str] = construct_polymer_str_extentions(data[2:])
    polymer_dict_extention: Dict[str, str] = construct_polymer_dict_extentions(data[2:])


    print("part 1 - Polymer value after 10 iterations:", adv14_1(polymer_template, polymer_str_extention))
    print("part 2 - Polymer value after 40 iterations:", adv14_2(polymer_template, polymer_dict_extention))

if __name__ == '__main__':
    main()
