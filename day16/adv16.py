#!/usr/bin/env python3

def adv16_1(binary_message: str):

    """
    while binary has any data, pop what is needed from the front and analyze
        first read header - 6 bits that is version and type id
            make function to handle this
        read package - look at the first bit in all 5 bit groups
            if 1 read on, if 0 last part stop after 4 bit payload
        read padding - one or more 0 added if needed after last group, read so that entire message is multiple of 4

        start over, remove bits as you go along
    """


def adv16_2():
    pass


def main():
    data = []
    with open("bits_data.txt") as f:
        data = f.readlines()
    f.close

    binary = ''
    for hex in data[0]:
        binary += str("{0:04b}".format(int(hex, 16)))

    print("part 1 - :", adv16_1(binary))
    print("part 2 - :", adv16_2())

if __name__ == '__main__':
    main()
