#!/usr/bin/env python3

from typing import List


def adv9_1(rope_movements: List[str]):
    head = (0,0)
    tail = (0,0)
    tail_positions = []
    # read moves
        # move head
        # move tail to cach up, diagonaly first if needed
        # add all pos to list
    # count tail pos with set()
    return


def adv9_2():
    return


def main():

    rope_movements = []
    with open("rope_data.txt") as f:
        rope_movements = f.read().splitlines()
    f.close()

    print("part 1 - :", adv9_1(rope_movements))
    print("part 2 - :", adv9_2())

if __name__ == '__main__':
    main()
