#!/usr/bin/env python3

from typing import List, Tuple
import re

def get_calibration_value (line: str) -> Tuple[int, int]:
    numbers = tuple(char for char in line if char.isdigit())
    return int(numbers[0] + numbers[-1])

def adv1_1(lines: List[str]) -> int:
    sum = 0
    for line in lines:
        sum += get_calibration_value(line)
    return sum


def adv1_2(liness: List[str]) -> int:
    sum = 0
    for line in lines:
        nums = tuple()

def main():

    lines = []
    with open("calibration_data.txt") as f:
        lines = f.read().splitlines()
    f.close()

    # elf_calories = convert_calorie_data(lines)
    # compressed_calories = sum_calories(elf_calories)

    print("part 1 - sum of all calibration values: ", adv1_1(lines))
    # print("part 2 - max calories carried by three elfs: ", adv1_2(compressed_calories))


if __name__ == '__main__':
    main()