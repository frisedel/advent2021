#!/usr/bin/env python3

from collections import namedtuple
from typing import Dict, List

Movement = namedtuple("Movement", ["direction", "amount"])

def move_head(head: Dict[str, int], move: Movement) -> None:
    if move.direction == "R":
        head["x"] += move.amount
    elif move.direction == "L":
        head["x"] -= move.amount
    elif move.direction == "U":
        head["y"] += move.amount
    elif move.direction == "D":
        head["y"] -= move.amount
    else:
        raise Exception("the rope exploded, blame the elves")


def move_tail(head: Dict[str, int], tail: Dict[str, int], tail_positions: List[str]) -> None:
    if abs(head["x"] - tail["x"]) <= 1 and abs(head["y"] - tail["y"]) <= 1:
        return

    if tail["x"] < head["x"]:
        tail["x"] += 1
    elif tail["x"] > head["x"]:
        tail["x"] -= 1

    if tail["y"] < head["y"]:
        tail["y"] += 1
    elif tail["y"] > head["y"]:
        tail["y"] -= 1

    tail_positions.append(f'{tail["x"]} {tail["y"]}')
    move_tail(head, tail, tail_positions)


def adv9_1(rope_movements: List[Movement]) -> int:
    head = {"x": 0, "y": 0}
    tail = {"x": 0, "y": 0}

    tail_positions = ["0 0"]

    for move in rope_movements:
        move_head(head, move)
        move_tail(head, tail, tail_positions)

    return len(set(tail_positions))


def move_rope(move: Movement, knots: List[Dict[str, int]], tail_positions: List[str]) -> None:
    for _ in range(move.amount):
        if move.direction == "R":
            knots[0]["x"] += 1
        elif move.direction == "L":
            knots[0]["x"] -= 1
        elif move.direction == "U":
            knots[0]["y"] += 1
        elif move.direction == "D":
            knots[0]["y"] -= 1
        for prev, cur in zip(knots, knots[1:]):
            while (abs(cur["x"] - prev["x"]) > 1 or abs(cur["y"] - prev["y"]) > 1):
                cur["x"] += (cur["x"] < prev["x"]) - (prev["x"] < cur["x"])
                cur["y"] += (cur["y"] < prev["y"]) - (prev["y"] < cur["y"])
        tail_positions.append(f'{knots[-1]["x"]} {knots[-1]["y"]}')


def adv9_2(rope_movements: List[Movement]) -> int:
    knots = [{"x": 0, "y": 0} for _ in range(10)]
    tail_positions = ["0 0"]

    for move in rope_movements:
        move_rope(move, knots, tail_positions)

    return len(set(tail_positions))


def extract_movements(rope_data: List[str]) -> List[Movement]:
    movements: List[Movement] = []
    for line in rope_data:
        direction, amount = line.split()
        movements.append(Movement(direction, int(amount)))
    return movements


def main():

    rope_data: List[str] = []
    with open("rope_data.txt") as f:
        rope_data = f.read().splitlines()
    f.close()

    rope_movements = extract_movements(rope_data)

    print("part 1 - Number of unique tail positions:", adv9_1(rope_movements))
    print("part 2 - Number of unique tail positions for snapped rope:", adv9_2(rope_movements))

if __name__ == '__main__':
    main()
