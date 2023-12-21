#!/usr/bin/env python3

from typing import List, Tuple, Union
import re

def get_calibration_value (line: str) -> Tuple[int, int]:
    numbers = tuple(char for char in line if char.isdigit())
    return int(numbers[0] + numbers[-1])

def adv1_1(lines: List[str]) -> int:
    sum = 0
    for line in lines:
        sum += get_calibration_value(line)
    return sum


def adv1_2(lines: List[str]) -> int:
    def get_number(x: Union[int, str]):
        return x if x.isdigit() else str(string_numbers.index(x))
    
    string_numbers = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    number_regex = r'(?=(one|two|three|four|five|six|seven|eight|nine|\d))'
    sum = 0

    for line in lines:
        numbers = re.findall(number_regex, line)
        sum += int(get_number(numbers[0]) + get_number(numbers[-1]))

    return sum

def main():

    lines = []
    with open("calibration_data.txt") as f:
        lines = f.read().splitlines()
    f.close()

    print("part 1 - sum of all calibration values: ", adv1_1(lines))
    print("part 2 - sum of all new calibration values: ", adv1_2(lines))


if __name__ == '__main__':
    main()