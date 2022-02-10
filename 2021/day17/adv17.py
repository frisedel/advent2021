#!/usr/bin/env python3

import re
from typing import Dict

def get_vy_max(y_min: int):
    return abs(y_min)


def get_y_max(y_min: int):
    return sum(range(get_vy_max(y_min)))


def adv17_1(target_area: Dict[str, int]):
    return get_y_max(target_area["y_min"])


def get_vx_min(x_min: int):
    vx_min = 0
    while True:
        if sum(range(vx_min)) >= x_min:
            return vx_min
        vx_min += 1


def can_hit_target_area(vx: int, vy: int, taget_area: Dict[str, int]):
    x = 0
    y = 0
    while True:
        if x > taget_area["x_max"] or y < taget_area["y_min"]:
            return False
        if vx == 0 and not taget_area["x_min"] <= x <= taget_area["x_max"]:
            return False

        if taget_area["x_min"] <= x <= taget_area["x_max"] and taget_area["y_min"] <= y <= taget_area["y_max"]:
            return True

        x += vx
        y += vy

        if vx > 0:
            vx -= 1
        vy -= 1


def adv17_2(target_area: Dict[str, int]):
    vx_min = get_vx_min(target_area["x_min"])
    vx_max = target_area["x_max"]
    vy_max = get_vy_max(target_area["y_min"])

    distinct_volocitys = 0

    for vx in range(vx_min-1, vx_max+1):
        for vy in range(-vy_max, vy_max+1):
            distinct_volocitys += can_hit_target_area(vx, vy, target_area)

    return distinct_volocitys


def calculate_target_area(target_data:str) -> Dict[str, int]:
    x_min, x_max = re.search(r'x=(-?\d+)..(-?\d+)', target_data).group(1, 2)
    y_min, y_max = re.search(r'y=(-?\d+)..(-?\d+)', target_data).group(1, 2)
    return {"x_min": int(x_min), "x_max": int(x_max), "y_min": int(y_min), "y_max": int(y_max)}


def main():
    with open('target_area.txt', 'r') as f:
        data = f.read().rstrip()

    target_area = calculate_target_area(data)

    print("part 1 - Max height of trajectory:", adv17_1(target_area))
    print("part 2 - Number of possible shots:", adv17_2(target_area))

if __name__ == '__main__':
    main()
