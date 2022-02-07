#!/usr/bin/env python3

def adv17_1():
    pass


def adv17_2():
    pass


def create_target_area(data:str):
    pass


def main():
    with open('target_area.txt', 'r') as f:
        data = f.read().rstrip()

    target_area = create_target_area(data)

    print("part 1 - :", adv17_1())
    print("part 2 - :", adv17_2())

if __name__ == '__main__':
    main()
