#!/usr/bin/env python3

from typing import Dict, List

def adv3_1(schematics: List[str]) -> int:
    sum = 0

    return sum

def adv3_2(games: List[str]) -> int:
    sum = 0

    return sum

def main():

    lines = []
    with open("games.txt") as f:
        lines = f.read().splitlines()
    f.close()

    print("part 1 - sum of part numbers: ", adv3_1(lines))
    print("part 2 - sum of : ", adv3_2(lines))


if __name__ == '__main__':
    main()