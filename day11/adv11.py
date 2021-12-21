#!/usr/bin/env python3

from typing import List

def adv11_1():
    pass


def adv11_2():
    pass


def main():
    octopus_data = []
    with open("octopus_grid.txt") as f:
        octopus_data = f.readlines()
    f.close

    print("part 1 - :", adv11_1())
    print("part 2 - :", adv11_2())

if __name__ == '__main__':
    main()
