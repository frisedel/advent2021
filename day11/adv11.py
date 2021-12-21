#!/usr/bin/env python3

from typing import Dict, List, Tuple

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

def point_exist(x_y: Tuple[int, int], octopus_grid: List[List[Dict[str, int]]]) -> bool:
    max_x = len(octopus_grid)-1
    max_y = len(octopus_grid[0])-1
    return 0 <= x_y[0] <= max_x and 0 <= x_y[1] <= max_y


def energy_spread(octopus_grid: List[List[Dict[str, int]]], iteration: int, octopus: Dict[str, int]):
    #   [.....]
    #   [-abc-]
    #   [-dXe-]
    #   [-fgh-]
    #   [.....]

    a = (octopus["x"]-1, octopus["y"]-1)
    b = (octopus["x"], octopus["y"]-1)
    c = (octopus["x"]+1, octopus["y"]-1)
    d = (octopus["x"]-1, octopus["y"])
    e = (octopus["x"]+1, octopus["y"])
    f = (octopus["x"]-1, octopus["y"]+1)
    g = (octopus["x"], octopus["y"]+1)
    h = (octopus["x"]+1, octopus["y"]+1)

    to_flas_next = []
    if point_exist(a, octopus_grid):
        oct_a = octopus_grid[a[0]][a[1]]
        oct_a["value"] += 1
        if oct_a["value"] > 9:
            oct_a["flash num"] += 1
            oct_a["last flash"] = iteration
            oct_a["value"] = 0
            to_flas_next.append(oct_a)
    #if b-h
    return to_flas_next

def process_iteration(octopus_grid: List[List[Dict[str, int]]], iteration: int, to_flash: List[Dict[str, int]]):
    for_next = []
    for octopus in to_flash:
        to_flash_next = energy_spread(octopus_grid, iteration, octopus)
        print(to_flash_next)
        for tfn in to_flash_next:
            for_next.append(tfn)
    if len(for_next) == 0:
        return None
    else:
        return process_iteration(octopus_grid, iteration, for_next)


def observe_flashes(octopus_grid: List[List[Dict[str, int]]], iterations):
    for iteration in range(iterations):
        to_flash: List[Dict[str, int]] = []
        for line in octopus_grid:
            for octopus in line:
                octopus["value"] += 1
                if octopus["value"] > 9:
                    octopus["flash num"] += 1
                    octopus["last flash"] = iteration
                    octopus["value"] = 0
                    to_flash.append(octopus)
        process_iteration(octopus_grid, iteration, to_flash)


def adv11_1(octopus_data: List[List[int]]):
    octopus_grid = create_grid(octopus_data)
    observe_flashes(octopus_grid, 100)
    print(octopus_grid)
    number_of_flashes = 0

    return number_of_flashes


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
