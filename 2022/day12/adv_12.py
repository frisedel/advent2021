#!/usr/bin/env python3

from typing import List


def adv12_1():
    return


def adv12_2():
    return


def main():

    topology_data: List[str] = []
    with open("topology_data.txt") as f:
        topology_data = f.read().splitlines()
    f.close()

    print("part 1 - :", adv12_1())
    print("part 2 - :", adv12_2())


if __name__ == '__main__':
    main()
