#!/usr/bin/env python3

from typing import Dict, List

def process_lantern_generations(lanterns_data: List[int], last_generation: int) -> Dict[int, int]:

    lanterns = { 0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0 }

    for lantern in lanterns_data:
        lanterns[lantern] += 1

    for index in range(last_generation):
        new_lanterns = { 0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0 }
        for lantern in lanterns:
            if lantern == 0:
                new_lanterns[6] = new_lanterns[6] + lanterns[0]
                new_lanterns[8] = new_lanterns[8] + lanterns[0]
            else:
                new_lanterns[lantern-1] = new_lanterns[lantern-1] + lanterns[lantern]
        lanterns = new_lanterns

    return lanterns


def count_lanterns(lanterns: Dict[int, int]) -> int:
    amount = 0
    for lantern in lanterns:
        amount += lanterns[lantern]
    return amount


def adv6_1(lanterns_data: List[int]) -> int:
    lantern_generations = process_lantern_generations(lanterns_data, 80)
    return count_lanterns(lantern_generations)


def adv6_2(lanterns: List[int]) -> int:
    lanterns = process_lantern_generations(lanterns, 256)
    return count_lanterns(lanterns)


def main():
    lantern_data = []
    with open("lanternfish_data.txt") as f:
        data = f.read().strip()
        lantern_data = data.split(",")
    f.close

    lanterns: List[int] = []
    for fish in lantern_data:
        lanterns.append(int(fish))

    print("part 1 - number of lanternfish after 80 days:", adv6_1(lanterns))
    print("part 2 - number of lanternfish after 256 days:", adv6_2(lanterns))

if __name__ == '__main__':
    main()
