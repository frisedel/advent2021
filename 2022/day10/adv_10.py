#!/usr/bin/env python3

from typing import List


def check_cycle(cycle: int, register_X: int, signal_strengths: List[int]) -> None:
    if (cycle - 20) % 40 == 0:
            signal_strengths.append(cycle * register_X)


def adv10_1(cycle_data: List[str]) -> int:
    cycle = 1
    register_X = 1
    signal_strenghts: List[int] = []
    for data in cycle_data:
        check_cycle(cycle, register_X, signal_strenghts)
        if data != "noop":
            cycle += 1
            check_cycle(cycle, register_X, signal_strenghts)
            _, value = data.split(" ")
            register_X += int(value)
        cycle += 1

    return sum(signal_strenghts)


def adv10_2(cycle_data: List[str]):
    cycle = 0
    register_X = 1
    CRT_screen = ["." * 40 for _ in range(6)]
    for data in cycle_data:
        if data != "noop":
            # draw pixel if register_X has the same value as cyckle % 40 or something, either here or after cycle += 1
            cycle += 1
            _, value = data.split(" ")
            register_X += int(value)
        # draw pixel if register_X has the same value as cyckle % 40 or something, either here or after cycle += 1
        cycle += 1
        return

    return


def main():

    cycle_data: List[str] = []
    with open("cycle_data.txt") as f:
        cycle_data = f.read().splitlines()
    f.close()

    print("part 1 - Sum of the six signal strengths:", adv10_1(cycle_data))
    print("part 2 - :", adv10_2(cycle_data))

if __name__ == '__main__':
    main()
