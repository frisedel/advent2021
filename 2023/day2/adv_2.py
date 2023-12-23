#!/usr/bin/env python3

from typing import Dict, List, Tuple, Union

def adv2_1(games: List[str]) -> int:
    max_colors: Dict = {
        "red": 12,
        "green": 13,
        "blue": 14
    }

    sum = 0
    for index, line in enumerate(games):
        game = index + 1
        legal_game = True
        hands = line.split(": ")[1].split("; ")
        for hand in hands:
            # legal_hand = True
            for colors in hand.split(", "):
                value, *_, color = colors.split(" ")
                if max_colors[color] < int(value):
                    legal_game = False
                    # print("Eh")
                # print(color, value)
        if legal_game:
            sum += game




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