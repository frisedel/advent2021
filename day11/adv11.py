#!/usr/bin/env python3

from typing import Dict, List

def create_grid(octopus_data: List[List[int]]):
    oct_grid: List[List[Dict[str, int]]] = []
    for line in octopus_data:
        oct_line: List[Dict[str, int]] = []
        for value in line:
            oct_line.append({"value": value, "last flash": 0, "flash num": 0})
        oct_grid.append(oct_line)
    return oct_grid


def adv11_1(octopus_data: List[List[int]]):
    octopus_grid = create_grid(octopus_data)
    """
        1. iterate over grid adding 1 untill above 9. ie when 10 set to 0
        2. make turning at 10 add 1 to all adjacent octopuses. use logic from day 9 but add diagonals as well
            a flash turns octopus to 0, but can be counted up again by neighbours the same round
            next iteration does not mean it is 0 then
    """


def adv11_2():
    pass


def main():
    data = []
    with open("octopus_grid.txt") as f:
        data = f.readlines()
    f.close

    octopus_data: List[List[int]] = []
    for line in data:
        octopus_data.append([int(i) for i in list(line.strip())])

    print("part 1 - :", adv11_1(octopus_data))
    print("part 2 - :", adv11_2())

if __name__ == '__main__':
    main()
