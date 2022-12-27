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


def write_CRT(register_X: int, cycle: int, CRT_screen: List[List[str]]) -> None:
    if register_X - 1 <= cycle % 40 <= register_X + 1:
        CRT_screen[cycle // 40][cycle % 40] = '#'


def adv10_2(cycle_data: List[str]):
    cycle = 0
    register_X = 1
    CRT_screen = [[" "] * 40 for _ in range(6)]

    for data in cycle_data:
        write_CRT(register_X, cycle, CRT_screen)
        if data != "noop":
            cycle += 1
            write_CRT(register_X, cycle, CRT_screen)
            _, value = data.split(" ")
            register_X += int(value)
        cycle += 1

    return CRT_screen


def main():

    cycle_data: List[str] = []
    with open("cycle_data.txt") as f:
        cycle_data = f.read().splitlines()
    f.close()

    print("part 1 - Sum of the six signal strengths:", adv10_1(cycle_data))
    CRT_screen = adv10_2(cycle_data)
    print("part 2 - CRT screen output:")
    for line in CRT_screen:
        print("".join(line))

if __name__ == '__main__':
    main()
