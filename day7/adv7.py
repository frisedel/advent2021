#!/usr/bin/env python3

from typing import Dict, List
import sys

def adv7_1(crabs_data: List[int]) -> int:
    crabs = crabs_data[:]
    crabs.sort()
    crab_max = max(crabs)
    crab_min = min(crabs)

    crabs_grouped: Dict[int, int] = {}

    for crab in crabs:
        if crab not in crabs_grouped.keys():
            crabs_grouped[crab] = 1
        else:
            crabs_grouped[crab] += 1

    min_fuel = sys.maxsize

    # for i in range(crab_min, crab_max):
    #     fuel_cost = 0
    #     loop over every crab group in dict and calc the fuel from that position. muliply by amount for that group
    #     for j in something

    print(crabs_grouped)

def main():
    crab_data = []
    with open("crabs.txt") as f:
        data = f.read().strip()
        crab_data = data.split(",")
    f.close

    crabs: List[int] = []
    for crab in crab_data:
        crabs.append(int(crab))

    print(len(crabs))
    print(max(crabs))

    print("part 1 - crabs to converge at:", adv7_1(crabs))
    # print("part 2 - number of lanternfish after 256 days:", adv6_2(lanterns))
    pass

if __name__ == '__main__':
    main()