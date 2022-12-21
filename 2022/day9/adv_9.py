#!/usr/bin/env python3

from collections import namedtuple
from typing import Dict, List

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
    knots = [{"x": 0, "y": 0} for _ in range(9)]
    knots_positions = [["0 0"] for _ in range(9)]

    for move in rope_movements:
        move_head(head, move)
        move_tail(head, knots[0], knots_positions[0])
        move_tail(knots[0], knots[1], knots_positions[1])
        move_tail(knots[1], knots[2], knots_positions[2])
        move_tail(knots[2], knots[3], knots_positions[3])
        move_tail(knots[3], knots[4], knots_positions[4])
        move_tail(knots[4], knots[5], knots_positions[5])
        move_tail(knots[5], knots[6], knots_positions[6])
        move_tail(knots[6], knots[7], knots_positions[7])
        move_tail(knots[7], knots[8], knots_positions[8])

    return len(set(knots_positions[-1]))


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

    test_large = extract_movements(["R 5", "U 8", "L 8", "D 3", "R 17", "D 10", "L 25", "U 20"])

    print("part 1 - Number of unique tail positions:", adv9_1(rope_movements))
    print("part 2 - :", adv9_2(rope_movements))

if __name__ == '__main__':
    main()
