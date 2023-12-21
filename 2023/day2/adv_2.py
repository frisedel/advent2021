#!/usr/bin/env python3

from typing import List, Tuple, Union

def adv2_1(lines: List[str]) -> int:
    max_red = 12
    max_green = 13
    mab_blue = 14

    for index, line in enumerate(lines[:2]):
        game = index + 1
        hands = line.split(": ")[1].split("; ")
        for hand in hands:
            print(hand.split(", "))
        print(game, hands)


    sum = 0
    return sum

def main():

    lines = []
    with open("games.txt") as f:
        lines = f.read().splitlines()
    f.close()

    print("part 1 - sum of possible games: ", adv2_1(lines))
    # print("part 2 - sum of all new calibration values: ", adv1_2(lines))


if __name__ == '__main__':
    main()