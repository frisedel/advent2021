#!/usr/bin/env python3

from typing import Dict, List
import sys

def get_crab_map(crabs_data: List[int]) -> Dict[int, int]:
    crabs = crabs_data[:]
    crabs.sort()
    crabs_grouped: Dict[int, int] = {}

    for crab in crabs:
        if crab not in crabs_grouped.keys():
            crabs_grouped[crab] = 1
        else:
            crabs_grouped[crab] += 1

    return crabs_grouped


def calc_fuel_to_point(dist: int, fule_rate: str):
    if fule_rate == "linear":
        return dist
    elif fule_rate == "increasing":
        fuel = 0
        for point in range(dist+1):
            fuel += point
        return fuel


def calc_min_fuel(crabs_data: List[int], fule_rate: str):
    crabs_grouped = get_crab_map(crabs_data)
    crab_max = max(crabs_data)
    crab_min = min(crabs_data)
    min_fuel = sys.maxsize
    for point in range(crab_min, crab_max+1):
        total_fuel_to_point = 0
        for crab in crabs_grouped:
            dist = abs(crab - point)
            number_of_crabs = crabs_grouped[crab]
            crab_fuel = calc_fuel_to_point(dist, fule_rate) * number_of_crabs
            total_fuel_to_point += crab_fuel
        if total_fuel_to_point < min_fuel:
            min_fuel = total_fuel_to_point
    return min_fuel


def adv7_1(crabs_data: List[int]) -> int:
    min_fuel = calc_min_fuel(crabs_data, "linear")
    return min_fuel


def adv7_2(crabs_data: List[int]):
    min_fuel = calc_min_fuel(crabs_data, "increasing")
    return min_fuel


def main():
    crab_data = []
    with open("crabs.txt") as f:
        data = f.read().strip()
        crab_data = data.split(",")
    f.close

    crabs: List[int] = []
    for crab in crab_data:
        crabs.append(int(crab))

    print("part 1 - min fuel for crabs on linear consumption:", adv7_1(crabs))
    print("part 2 - min fuel for crabs on increasing consumption:", adv7_2(crabs))
    pass

if __name__ == '__main__':
    main()