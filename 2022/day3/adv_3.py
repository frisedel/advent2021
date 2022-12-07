#!/usr/bin/env python3

from typing import Dict, List, Tuple
import string

def search_rucksack(rucksack: Tuple[str, str]) -> List[str]:
    duplicates: List[str] = []
    for item in rucksack[0]:
        if item in rucksack[1]:
            duplicates.append(item)
    return duplicates


def find_duplicates(rucksacks: List[Tuple[str, str]]):
    duplicates = []
    for rucksack in rucksacks:
        duplicates.append(search_rucksack(rucksack))
    return [item for sublist in duplicates for item in sublist]

def adv3_1(rucksacks: List[Tuple[str, str]]):
    duplicates = find_duplicates(rucksacks)
    duplicate_map: Dict[str, int] = {}
    for item in duplicates:
        if item not in duplicate_map:
            duplicate_map[item] = 1
        else:
            duplicate_map[item] += 1
    priority = list(zip(string.ascii_lowercase, range(1, 27))) + list(zip(string.ascii_uppercase, range(27, 53)))

    return


def adv3_2():
    return


def split_content(content: str) -> Tuple[str, str]:
    half_length = int(len(content)/2)
    return content[:half_length], content[half_length:-1]


def create_rucksacks(rucksack_data: List[str]) -> List[Tuple[str, str]]:
    rucksacks: List[Tuple[str, str]] = []
    for data in rucksack_data:
        rucksacks.append(split_content(data))
    return rucksacks


def main():

    lines = []
    with open("rucksack_content.txt") as f:
        lines = f.readlines()
    f.close()

    rucksacks = create_rucksacks(lines)

    print("part 1 - : ", adv3_1(rucksacks))
    print("part 2 - : ", adv3_2())


if __name__ == '__main__':
    main()
