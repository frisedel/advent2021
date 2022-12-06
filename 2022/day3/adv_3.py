#!/usr/bin/env python3

def adv3_1():
    return


def adv3_2():
    return


def main():

    lines = []
    with open("rucksack_content.txt") as f:
        lines = f.readlines()
    f.close()

    print("part 1 - : ", adv3_1())
    print("part 2 - : ", adv3_2())


if __name__ == '__main__':
    main()
