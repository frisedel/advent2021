#!/usr/bin/env python3

from typing import List, Tuple

def fully_contains(pair: List[Tuple[int]]):
    return pair[0][0] <= pair[1][0] <= pair[0][1] and pair[0][0] <= pair[1][1] <= pair[0][1] or pair[1][0] <= pair[0][0] <= pair[1][1] and pair[1][0] <= pair[0][1] <= pair[1][1]

def adv4_1(assignment_pairs: List[List[Tuple[int]]]) -> int:
    count = 0
    for pair in assignment_pairs:
        if fully_contains(pair):
            count += 1
    return count


def adv4_2() -> int:
    return

def create_pairs(assignments_data: List[str]) -> List[Tuple[int]]:
    return [[tuple(map(int, area.split("-"))) for area in assignments.split(",")] for assignments in assignments_data]

def main():

    assignments_data = []
    with open("assignments.txt") as f:
        assignments_data = f.read().splitlines()
    f.close()

    assignment_pairs = create_pairs(assignments_data)

    print("part 1 - Amount of areas fully inside other area:", adv4_1(assignment_pairs))
    print("part 2 - :", adv4_2())


if __name__ == '__main__':
    main()
