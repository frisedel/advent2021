#!/usr/bin/env python3

def adv16_1(binary_message: str):
    """
    while binary has any data, pop what is needed from the front and analyze
        first read header - 6 bits that is version and type id
            version - no info on different versions. add them up for part 1
            type id -
                type id 4 - it is a literal value split over multiple parts. keep going untill the latest 5 bits start with zero
                type id 0 - next 15 bits gives the length of the subpackages
                type id 1 - next 11 bits gives the length of the subpackages

            make function to handle this
        read package - look at the first bit in all 5 bit groups
            if 1 read on, if 0 last part stop after 4 bit payload
        read padding - one or more 0 added if needed after last group, read so that entire message is multiple of 4

        start over, remove bits as you go along
    """

    """
    read header, first 3 bits is version add that numbver to total
    check version
        if 4 - read and count bits untill the group of 5 starts with 0. read bits so that message is multiple of 4
        if 0 - read next 15 bits as number, and read all thouse to total of message then add zeros as needed
        if 1 - read next 11 bits as number, and read all thouse to total of message then add zeros as needed
    next header starts now, repeat
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
