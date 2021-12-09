#!/usr/bin/env python3

from typing import List

def clean_last_generation(lanterns: List[int], prev_gen: List[int]) -> List[int]:
    cleaned: List[int] = []
    for index in range(len(lanterns)):
        if lanterns[index] == 7:
            if prev_gen[index] == 8:
                cleaned.append(7)
            else:
                cleaned.append(0)
        else:
            cleaned.append(lanterns[index])
    return cleaned

def process_lantern_generations(lanterns: List[int], prev_gen: List[int], generation_cap: int, last_generation: int) -> List[int]:
    if last_generation == generation_cap:
        return clean_last_generation(lanterns, prev_gen)

    old_lanterns: List[int] = []
    new_lanterns: List[int] = []

    for lantern in lanterns:
        if lantern == 0:
            old_lanterns.append(6)
            new_lanterns.append(8)
        else:
            old_lanterns.append(lantern-1)

    all_lanterns = [*old_lanterns, *new_lanterns]
    print(last_generation, len(all_lanterns))
    return process_lantern_generations(all_lanterns, lanterns, generation_cap, last_generation+1)


def adv6_1(lanterns_numbers: List[int]):
    lantern_generations = process_lantern_generations(lanterns_numbers, [], 80, 0)
    return len(lantern_generations)


def main():
    lantern_data = []
    with open("lanternfish_data.txt") as f:
        data = f.read().strip()
        lantern_data = data.split(",")
    f.close

    lanterns: List[int] = []
    for fish in lantern_data:
        lanterns.append(int(fish))

    print("part 1 - number of lanternfish:", adv6_1(lanterns))
    #print("part 2 - :", adv6_2())

if __name__ == '__main__':
    main()
