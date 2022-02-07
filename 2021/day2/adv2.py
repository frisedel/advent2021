#!/usr/bin/env python3

from typing import List, Tuple

def adv2_1(path: List[Tuple[str, int]]):
    depth = 0
    forward = 0

    for command, amount in path:
        if command == "forward":
            forward += amount
        if command == "down":
            depth += amount
        if command == "up":
            depth -= amount
    print("forward:", forward, "depth:", depth)

    return forward * depth


def adv2_2(path: List[Tuple[str, int]]):
    depth = 0
    forward = 0
    aim = 0

    for command, amount in path:
        if command == "down":
            aim += amount
        if command == "up":
            aim -= amount
        if command == "forward":
            forward += amount
            depth += aim * amount
    print("forward:", forward, "depth:", depth, "aim:", aim)

    return forward * depth


def main():
    lines = []
    with open("path_commands.txt") as f:
        lines = f.readlines()
    f.close()

    path_commands: List[Tuple[str, int]] = []
    for line in lines:
        commands = line.split()
        path_commands.append((commands[0], int(commands[1])))

    print("part 1:", adv2_1(path_commands))
    print("part 2:", adv2_2(path_commands))


if __name__ == '__main__':
    main()
