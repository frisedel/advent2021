#!/usr/bin/env python3

from ast import literal_eval
from typing import List

class Sailfish_number:
    def __init__(self, left: int or List[int], right: int or List[int]):
        self.left: int or Sailfish_number = None
        self.right: int or Sailfish_number = None
        if type(left) == list:
            self.left = Sailfish_number(left[0], left[1])
        else:
            self.left = left
        if type(right) == list:
            self.right = Sailfish_number(right[0], right[1])
        else:
            self.right = right
        print(self.left, self.right)


def adv18_1(numbers: List[int or Sailfish_number]):
    pass


def adv18_2():
    pass


def main():
    data = []
    with open('snailfish_numbers.txt') as f:
        data = f.readlines()
    f.close

    numbers = []
    for line in data:
        sfn = literal_eval(line)
        numbers.append(Sailfish_number(sfn[0], sfn[1]))

    print("part 1 - :", adv18_1(numbers))
    print("part 2 - :", adv18_2())

if __name__ == '__main__':
    main()
