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
        raise Exception("not a move")


def move_tail(head: Dict[str, int], tail: Dict[str, int]):
    x_diff = abs(head["x"] - tail["x"])
    y_diff = abs(head["y"] - tail["y"])

    if x_diff <= 1 and y_diff <= 1: # head next to tail, no move needed
        return

    elif y_diff == 0:                 # move on x axis
        if tail["x"] < head["x"]:
            for _ in range(x_diff-1):
                tail["x"] += 1
        else:
            for _ in range(x_diff-1):
                tail["x"] -= 1

    elif x_diff == 0:                 # move on y axis
        if tail["y"] < head["y"]:
            for _ in range(y_diff-1):
                tail["y"] += 1
        else:
            for _ in range(y_diff-1):
                tail["y"] -= 1

    elif x_diff >= 1 and y_diff >= 1:   # move on both axis
        # for step in move
            # if head X > tail X tail X ++
            # if head X < tail X tail X --
        return
    return


def adv9_1(rope_movements: List[str]):
    head = {"x": 0, "y": 0}
    tail = {"x": 0, "y": 0}

    tail_positions = []

    for move in rope_movements:
        move_head(head, move)
        print("h", head, "t", tail)
        move_tail(head, tail)
        print("t", tail)

    return


def adv9_2():
    return


def main():

    rope_movements: List[Movement] = []
    with open("rope_data.txt") as f:
        for line in f:
            direction, amount = line.split()
            rope_movements.append(Movement(direction, int(amount)))
    f.close()

    print("part 1 - :", adv9_1(rope_movements[:5]))
    print("part 2 - :", adv9_2())

if __name__ == '__main__':
    main()
