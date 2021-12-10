#!/usr/bin/env python3

from typing import List

def main():
    crab_data = []
    with open("crabs.txt") as f:
        data = f.read().strip()
        crab_data = data.split(",")
    f.close

    crabs: List[int] = []
    for crab in crab_data:
        crabs.append(int(crab))

    print(crabs)

    # print("part 1 - number of lanternfish after 80 days:", adv6_1(lanterns))
    # print("part 2 - number of lanternfish after 256 days:", adv6_2(lanterns))
    pass

if __name__ == '__main__':
    main()