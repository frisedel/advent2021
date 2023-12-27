#!/usr/bin/env python3

from typing import Dict, List

def adv2_1(games: List[str]) -> int:
    max_colors: Dict = {
        "red": 12,
        "green": 13,
        "blue": 14
    }

    sum = 0
    for game_index, game in enumerate(games, 1):
        legal_game = True
        hands = game.split(": ")[1].split("; ")
        for hand in hands:
            for colors in hand.split(", "):
                value, *_, color = colors.split(" ")
                if max_colors[color] < int(value):
                    legal_game = False
        if legal_game:
            sum += game_index

    return sum

def adv2_2(games: List[str]) -> int:
    sum = 0
    for game in games:
        min_colors: Dict = {
            "red": 0,
            "green": 0,
            "blue": 0
        }
        hands = game.split(": ")[1].split("; ")
        for hand in hands:
            for colors in hand.split(", "):
                value, *_, color = colors.split(" ")
                if min_colors[color] < int(value):
                    min_colors[color] = int(value)
        sum += min_colors["red"] * min_colors["green"] * min_colors["blue"]

    return sum

def main():

    lines = []
    with open("games.txt") as f:
        lines = f.read().splitlines()
    f.close()

    print("part 1 - sum of possible games: ", adv2_1(lines))
    print("part 2 - sum of all minimun cubes: ", adv2_2(lines))


if __name__ == '__main__':
    main()