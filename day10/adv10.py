#!/usr/bin/env python3

from typing import List


def adv10_1(syntax_data: List[str]):
    for d in syntax_data:
        print(d)

    pass

def adv10_2():
    pass

def main():
    input_data = []
    with open("syntax_input.txt") as f:
        input_data = f.readlines()
    f.close

    syntax_data = []
    for line in input_data:
        syntax_data.append(list(line.strip()))

    print("part 1 - :", adv10_1(syntax_data))
    print("part 2 - :", adv10_2())

if __name__ == '__main__':
    main()
