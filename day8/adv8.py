#!/usr/bin/env python3

from typing import Dict, List

def find_numbers(segment_data: List[str]):
    amount_numbers = {1:0, 4:0, 7:0, 8:0}
    others = 0
    for code in segment_data:
        signal_values = code.split('|')[-1].strip().split()
        for value in signal_values:
            if len(value) == 2:
                amount_numbers[1] += 1
            elif len(value) == 4:
                amount_numbers[4] += 1
            elif len(value) == 3:
                amount_numbers[7] += 1
            elif len(value) == 7:
                amount_numbers[8] += 1
            else:
                others += 1
    return amount_numbers


def count_numbers(numbers: Dict[int, int]):
    appearances = 0
    for number in numbers:
        appearances += numbers[number]
    return appearances


def adv8_1(segment_data: List[str]):
    amount_numbers = find_numbers(segment_data)
    number_of_appearances = count_numbers(amount_numbers)
    return number_of_appearances


def main():
    data = []
    with open("seven_segment.txt") as f:
        data = f.readlines()
    f.close

    segment_data: List[str] = []
    for code in data:
        segment_data.append(code.strip())


    print("part 1 - number of apperances:", adv8_1(segment_data))
    # print("part 2 - :", adv8_2())

if __name__ == '__main__':
    main()