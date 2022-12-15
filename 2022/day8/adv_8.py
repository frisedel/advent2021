#!/usr/bin/env python3

from typing import List
import numpy as np


def adv8_1(forest: np.ndarray) -> int:
    rows, columns = np.shape(forest)
    count = 0
    for x in range(1, rows-1):
        for y in range(1, columns-1):
            visible = False
            tree = forest[x,y]
            if tree > np.max(forest[0:x,:]):
                visible = True
            elif tree > np.max(forest[x:-1,:]):
                visible = True
            elif tree > np.max(forest[:,0:y]):
                visible = True
            elif tree > np.max(forest[:,y:-1]):
                visible = True
            if visible:
                count += 1
    return count


def adv8_2() -> int:
    return


def map_forest(forest_data: List[str]) -> np.ndarray:
    return np.array([[int(tree) for tree in line] for line in forest_data])


def main():

    forest_data = []
    with open("reforestation_data.txt") as f:
        forest_data = f.read().splitlines()
    f.close()

    forest = map_forest(forest_data)

    print("part 1 - :", adv8_1(forest))
    print("part 2 - :", adv8_2())

if __name__ == '__main__':
    main()

