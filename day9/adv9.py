#!/usr/bin/env python3

from typing import List

def adv9_1(data):
    pass

def adv9_2(data):
    pass

def main():
    input_data = []
    with open("smoke_map.txt") as f:
        input_data = f.readlines()
    f.close

    data: List[str] = []
    for code in input_data:
        data.append(code.strip())

    print(data)

    print("part 1 - :", adv9_1(data))
    print("part 2 - :", adv9_2(data))

if __name__ == '__main__':
    main()

"""
    === for first part ===
    1. read input
    2. convert to list of int
    3 loop over rows. if local low, take index and check above and below
    4. add low points to list
    5. calculate risk for points
    6. sum the risks
    7. return value
"""