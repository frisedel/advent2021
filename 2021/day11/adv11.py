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


def point_exist(x_y: Tuple[int, int], octopus_grid: List[List[Dict[str, int]]]) -> bool:
    max_x = len(octopus_grid)-1
    max_y = len(octopus_grid[0])-1
    return 0 <= x_y[0] <= max_x and 0 <= x_y[1] <= max_y


def handle_octopus(oct: Tuple[int, int], octopus_grid: List[List[Dict[str, int]]], iteration: int):
    if point_exist(oct, octopus_grid):
        octopus = octopus_grid[oct[0]][oct[1]]
        if octopus["value"] > 0:
            octopus["value"] += 1
            if octopus["value"] > 9:
                octopus["flash num"] += 1
                octopus["last flash"] = iteration
                octopus["value"] = 0
                return octopus
    return None


def energy_spread(octopus_grid: List[List[Dict[str, int]]], iteration: int, octopus: Dict[str, int]) -> List[Dict[str, int]]:
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
    to_flas_next.append(handle_octopus(a, octopus_grid, iteration))
    to_flas_next.append(handle_octopus(b, octopus_grid, iteration))
    to_flas_next.append(handle_octopus(c, octopus_grid, iteration))
    to_flas_next.append(handle_octopus(d, octopus_grid, iteration))
    to_flas_next.append(handle_octopus(e, octopus_grid, iteration))
    to_flas_next.append(handle_octopus(f, octopus_grid, iteration))
    to_flas_next.append(handle_octopus(g, octopus_grid, iteration))
    to_flas_next.append(handle_octopus(h, octopus_grid, iteration))

    return list(filter(None.__ne__, to_flas_next))


def process_iteration(octopus_grid: List[List[Dict[str, int]]], iteration: int, to_flash: List[Dict[str, int]]):
    for_next: List[Dict[str, int]] = []
    for octopus in to_flash:
        to_flash_next = energy_spread(octopus_grid, iteration, octopus)
        for tfn in to_flash_next:
            for_next.append(tfn)
    if len(for_next) == 0:
        return None
    else:
        return process_iteration(octopus_grid, iteration, for_next)


def observe_flashes(octopus_grid: List[List[Dict[str, int]]], iteration):
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
    for iteration in range(100):
        observe_flashes(octopus_grid, iteration)
    number_of_flashes = 0
    for line in octopus_grid:
        for octopus in line:
            number_of_flashes += octopus["flash num"]
    return number_of_flashes


def grid_syncronized(octopus_grid: List[List[Dict[str, int]]], iteration: int):
    for line in octopus_grid:
        for octopus in line:
            if octopus["last flash"] != iteration:
                return False
    return True


def adv11_2(octopus_data: List[List[int]]):
    octopus_grid = create_grid(octopus_data)
    synchronized = False
    iterations = 0
    while not synchronized:
        iterations += 1
        observe_flashes(octopus_grid, iterations)
        if grid_syncronized(octopus_grid, iterations):
            synchronized = True
    return iterations


def main():
    data = []
    with open("octopus_grid.txt") as f:
        data = f.readlines()
    f.close

    octopus_data: List[List[int]] = []
    for line in data:
        octopus_data.append([int(i) for i in list(line.strip())])

    print("part 1 - Number of flashes after 100 iterations:", adv11_1(octopus_data))
    print("part 2 - Iteration when octopuses syncronize for the first time:", adv11_2(octopus_data))

if __name__ == '__main__':
    main()
