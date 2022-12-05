#!/usr/bin/env python3

from typing import List


def sum_calories(elf_calories: List[List[int]]) -> List[int]:
    compressed_calories = []
    for elf in elf_calories:
        compressed_calories.append(sum(elf))
    return compressed_calories


def convert_calorie_data(calorie_data: List[str]) -> List[List[int]]:
    size = len(calorie_data)
    idx_list = [idx + 1 for idx, val in enumerate(calorie_data) if val == '\n']
    split_data = [calorie_data[i: j] for i, j in zip(
        [0] + idx_list, idx_list + ([size] if idx_list[-1] != size else [])
    )]

    elf_calories: List[List[int]] = []
    for data in split_data:
        elf_snacks: List[int] = []
        for snack in data:
            if snack != '\n':
                elf_snacks.append(int(snack.strip()))
        elf_calories.append(elf_snacks)

    return elf_calories


def adv1_1(elf_calories: List[int]) -> int:
    return max(elf_calories)


def adv1_2(elf_calories: List[int]) -> int:
    elf_calories.sort(reverse=True)
    top_three = elf_calories[:3]
    return sum(top_three)


def main():

    lines = []
    with open("calories.txt") as f:
        lines = f.readlines()
    f.close()

    elf_calories = convert_calorie_data(lines)
    compressed_calories = sum_calories(elf_calories)

    print("part 1 - max calories carried by one elf: ", adv1_1(compressed_calories))
    print("part 2 - max calories carried by three elfs: ", adv1_2(compressed_calories))


if __name__ == '__main__':
    main()
