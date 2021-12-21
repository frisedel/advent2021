#!/usr/bin/env python3

from typing import Dict, List

def create_grid(octopus_data: List[List[int]]) -> List[List[Dict[str, int]]]:
    oct_grid: List[List[Dict[str, int]]] = []
    for x in range(len(octopus_data)):
        oct_line: List[Dict[str, int]] = []
        for y in range(len(octopus_data[x])):
            oct_line.append({"x": x, "y": y, "value": octopus_data[x][y], "last flash": 0, "flash num": 0})
        oct_grid.append(oct_line)
    return oct_grid


"""
    func to recursively handle the iteration, or a while loop
    take grid, iteration number and a list of octopuses to process
    when list is empty go top next step in outer loop
"""

def process_iteration(octopus_grid: List[List[Dict[str, int]]], to_blink: List[Dict[str, int]], iteration: int, ):
    pass


def count_blinks(octopus_grid: List[List[Dict[str, int]]], iterations):
    for iteration in range(iterations):
        # to_blink: List[Dict[str, int]] = []
        # all octopuses +1 to count, if it goes to 10, set to 0 and add to to_blink
        # process_iteration(octopus_grid, to_blink, iteration)
        pass
    total = 0
    # count blinks in all octopuses
    return total


def adv11_1(octopus_data: List[List[int]]):
    octopus_grid = create_grid(octopus_data)
    number_blinks = count_blinks(octopus_grid, 100)

    """
        1. iterate over grid adding 1 untill above 9. ie when 10 set to 0
        2. make turning at 10 add 1 to all adjacent octopuses. use logic from day 9 but add diagonals as well
            a flash turns octopus to 0, but can be counted up again by neighbours the same round
            next iteration does not mean it is 0 then
    """
    return number_blinks


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
