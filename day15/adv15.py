#!/usr/bin/env python3

from typing import List

def adv15_1():
    """
    use A* to find optimal path
    total cost to next node/number should be the cost to go to that node plus distance to end where the latter is the heuristic value. distance is eiter straight line or steps
    possibly check frontier every loop for end before taking the one with the minimal cost
    """
    pass


def adv15_2():
    pass


def main():
    data = []
    with open("map_data_small.txt") as f:
        data = f.readlines()
    f.close

    """
    Map should be a List[List[MapNode]] so that coords, value and conections. MapNode is a class object.
    Use Lab1.py as template for this
    loop over range for lines and line where lines gives y and line gives x
    """
    map: List[List[int]] = []
    for line in data:
        row = []
        for value in line.strip():
            row.append(int(value))
        map.append(row)

    print("part 1 - Cost for path with lowest risk:", adv15_1())
    print("part 2 - :", adv15_2())

if __name__ == '__main__':
    main()
