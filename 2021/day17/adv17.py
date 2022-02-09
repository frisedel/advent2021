#!/usr/bin/env python3

import re
from typing import Dict

def adv17_1(target_area: Dict[str, int]):
    max_yv = abs(target_area["y_min"])-1
    return sum(range(1, max_yv+1))

def adv17_2():
    pass


def calculate_target_area(target_data:str) -> Dict[str, int]:
    x_min, x_max = re.search(r'x=(-?\d+)..(-?\d+)', target_data).group(1, 2)
    y_min, y_max = re.search(r'y=(-?\d+)..(-?\d+)', target_data).group(1, 2)
    return {"x_min": int(x_min), "x_max": int(x_max), "y_min": int(y_min), "y_max": int(y_max)}


def main():
    with open('target_area.txt', 'r') as f:
        data = f.read().rstrip()

    target_area = calculate_target_area(data)

    print("part 1 - Max height of trajectory:", adv17_1(target_area))
    print("part 2 - :", adv17_2())

if __name__ == '__main__':
    main()
