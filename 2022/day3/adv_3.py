#!/usr/bin/env python3

from typing import Dict, List, Tuple
import string

priority = dict(zip(string.ascii_lowercase+string.ascii_uppercase, range(1, 53)))

def search_rucksack(rucksack: Tuple[str, str]) -> List[str]:
    duplicates: List[str] = []
    for item in rucksack[0]:
        if item in rucksack[1]:
            duplicates.append(item)
    return list(set(duplicates))


def find_duplicates(rucksacks: List[Tuple[str, str]]) -> List[str]:
    duplicates = []
    for rucksack in rucksacks:
        duplicates.extend(search_rucksack(rucksack))
    return duplicates


def split_content(content: str) -> Tuple[str, str]:
    half_length = len(content)//2
    return content[:half_length], content[half_length:]


def create_rucksacks(rucksack_data: List[str]) -> List[Tuple[str, str]]:
    rucksacks: List[Tuple[str, str]] = []
    for data in rucksack_data:
        rucksacks.append(split_content(data))
    return rucksacks


def adv3_1(rucksack_data: List[str]) -> int:
    rucksacks = create_rucksacks(rucksack_data)
    duplicates = find_duplicates(rucksacks)

    count = 0
    for item in duplicates:
        count += priority[item]
    return count


def create_groups(elfs: List[str]) -> List[List[str]]:
    return [elfs[i:i+3] for i in range(0, len(elfs), 3)]


def find_badge(elf_group: List[str]) -> str:
    for item in elf_group[0]:
        if elf_group[1].find(item) != -1 and elf_group[2].find(item) != -1:
            return item
    raise Exception("Badge not found")


def adv3_2(elf_data: List[str]) -> int:
    elf_groups = create_groups(elf_data)

    badges: List[str] = [find_badge(group) for group in elf_groups]

    priority_sum = 0
    for badge in badges:
        priority_sum += priority[badge]
    return priority_sum


def main():

    rucksack_data = []
    with open("rucksack_content.txt") as f:
        rucksack_data = f.read().splitlines()
    f.close()

    print("part 1 - Sum of priority item types:", adv3_1(rucksack_data))
    print("part 2 - Sum of group priorities:", adv3_2(rucksack_data))


if __name__ == '__main__':
    main()
