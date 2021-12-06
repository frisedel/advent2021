#!/usr/bin/env python3

from typing import List

def adv1_1(values: List[int]):

    single_number_increse = 0
    previous = values[0]

    for value in values[1:]:
            if value > previous:
                single_number_increse += 1
            previous = value

    return single_number_increse


def adv1_2(values: List[int]):

    def calc_block(start: int):
        return values[start] + values[start+1] + values[start+2]

    block_number_increase = 0
    previous_block = calc_block(0)

    values_length = len(values)

    for index in range (1, values_length-2):
        block = calc_block(index)
        if block > previous_block:
            block_number_increase += 1
        previous_block = block

    return block_number_increase

def main():

    lines = []
    with open("depth.txt") as f:
        lines = f.readlines()
    f.close()
    values = [int(i) for i in lines]

    print("part 1 - sonar sweep measurements: ", adv1_1(values))
    print("part 2 - three-measurement sliding window: ", adv1_2(values))

if __name__ == '__main__':
    main()
