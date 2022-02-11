#!/usr/bin/env python3

def adv18_1():
    pass


def adv18_2():
    pass


def main():
    data = []
    with open('snailfish_numbers.txt') as f:
        data = f.readlines()
    f.close

    print("part 1 - :", adv18_1())
    print("part 2 - :", adv18_2())

if __name__ == '__main__':
    main()
