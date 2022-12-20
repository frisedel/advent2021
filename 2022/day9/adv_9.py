#!/usr/bin/env python3

from collections import namedtuple
from typing import Dict, List, Tuple

Movement = namedtuple("Movement", ["direction", "amount"])

def move_head(head: Dict[str, int], move: Movement):
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
    # x_diff = abs(head["x"] - tail["x"])
    # y_diff = abs(head["y"] - tail["y"])

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


def adv9_1(rope_movements: List[str]):
    head = {"x": 0, "y": 0}
    tail = {"x": 0, "y": 0}

    tail_positions = ["0 0"]

    for move in rope_movements:
        move_head(head, move)
        move_tail(head, tail, tail_positions)

    return len(set(tail_positions))


def adv9_2(rope_movements: List[str]):
    head = {"x": 0, "y": 0}
    knot1 = {"x": 0, "y": 0}
    knot2 = {"x": 0, "y": 0}
    knot3 = {"x": 0, "y": 0}
    knot4 = {"x": 0, "y": 0}
    knot5 = {"x": 0, "y": 0}
    knot6 = {"x": 0, "y": 0}
    knot7 = {"x": 0, "y": 0}
    knot8 = {"x": 0, "y": 0}
    knot9 = {"x": 0, "y": 0}

    knot1_positions = ["0 0"]
    knot2_positions = ["0 0"]
    knot3_positions = ["0 0"]
    knot4_positions = ["0 0"]
    knot5_positions = ["0 0"]
    knot6_positions = ["0 0"]
    knot7_positions = ["0 0"]
    knot8_positions = ["0 0"]
    knot9_positions = ["0 0"]

    for move in rope_movements:
        move_head(head, move)
        move_tail(head, knot1, knot1_positions)
        move_tail(knot1, knot2, knot2_positions)
        move_tail(knot2, knot3, knot3_positions)
        move_tail(knot3, knot4, knot4_positions)
        move_tail(knot4, knot5, knot5_positions)
        move_tail(knot5, knot6, knot6_positions)
        move_tail(knot6, knot7, knot7_positions)
        move_tail(knot7, knot8, knot8_positions)
        move_tail(knot8, knot9, knot9_positions)

    return len(set(knot9_positions))


def extract_movements(rope_data: List[str]):
    movements = []
    for line in rope_data:
        direction, amount = line.split()
        movements.append(Movement(direction, int(amount)))
    return movements


def main():

    rope_data: List[Movement] = []
    with open("rope_data.txt") as f:
        rope_data = f.read().splitlines()
    f.close()

    rope_movements = extract_movements(rope_data)

    print("part 1 - Number of unique tail positions:", adv9_1(rope_movements))
    print("part 2 - :", adv9_2(rope_movements))

if __name__ == '__main__':
    main()
