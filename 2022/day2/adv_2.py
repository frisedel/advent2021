#!/usr/bin/env python3

from typing import Callable, List


def get_points(round: str) -> int:
    if round == "BX":   #paper rock
        return 1        # 1 + 0
    elif round == "CY": #scissors paper
        return 2        # 2 + 0
    elif round == "AZ": #rock scissors
        return 3        # 3 + 0
    elif round == "AX": #rock rock
        return 4        # 1 + 3
    elif round == "BY": # paper paper
        return 5        # 2 + 3
    elif round == "CZ": #scissors scissors
        return 6        # 3 + 3
    elif round == "CX": #scissors rock
        return 7        # 1 + 6
    elif round == "AY": #rock paper
        return 8        # 2 + 6
    elif round == "BZ": #paper scissors
        return 9        # 3 + 6
    else:
        return 0


def get_corrected_points(round: str) -> int:
    if round == "BX":   #paper loose -> rock
        return 1        # 1 + 0
    elif round == "CX": #scissors loose -> paper
        return 2        # 2 + 0
    elif round == "AX": #rock loose -> scissors
        return 3        # 3 + 0
    elif round == "AY": #rock draw -> rock
        return 4        # 1 + 3
    elif round == "BY": # paper draw -> paper
        return 5        # 2 + 3
    elif round == "CY": #scissors draw -> scissors
        return 6        # 3 + 3
    elif round == "CZ": #scissors winn -> rock
        return 7        # 1 + 6
    elif round == "AZ": #rock winn -> paper
        return 8        # 2 + 6
    elif round == "BZ": #paper winn -> scissors
        return 9        # 3 + 6
    else:
        return 0


def convert_strategy(strategy_data: List[str], points_calculation: Callable[[str], int]) -> List[int]:
    game_points: List[int] = []
    for round in strategy_data:
        game_points.append(points_calculation(round))
    return game_points


def adv2_1(strategy: List[str]) -> int:
    game = convert_strategy(strategy, get_points)
    return sum(game)


def adv2_2(strategy: List[str]) -> int:
    game = convert_strategy(strategy, get_corrected_points)
    return sum(game)


def main():

    lines = []
    with open("strategy_guide.txt") as f:
        lines = f.read().splitlines()
    f.close()
    lines = [line.replace(' ', '') for line in lines]

    print("part 1 - total score for stategy guide: ", adv2_1(lines))
    print("part 2 - total score for corrected stategy guide: ", adv2_2(lines))


if __name__ == '__main__':
    main()
