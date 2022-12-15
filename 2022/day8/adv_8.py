#!/usr/bin/env python3

from typing import List
import numpy as np


def adv8_1(forest: np.ndarray) -> int:
    rows, columns = np.shape(forest)

    for x in range(0, rows):
        for y in range(0, columns):
            visible = False
            if forest[x,y] > np.max(forest[0:x,:]): #not working
                print("ello")
    return


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

