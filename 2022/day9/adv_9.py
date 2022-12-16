#!/usr/bin/env python3

def adv9_1():
    return


def adv9_2():
    return


def main():

    rope_movements = []
    with open("rope_data.txt") as f:
        rope_movements = f.read().splitlines()
    f.close()

    print("part 1 - :", adv9_1())
    print("part 2 - :", adv9_2())

if __name__ == '__main__':
    main()
