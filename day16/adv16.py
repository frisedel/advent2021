#!/usr/bin/env python3

def adv16_1(base_message: str):
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
        if 0 - read next 15 bits as number, this is the lenght of the next part
        if 1 - read next 11 bits as number, this is the lenght of the next part
    read correct amount of bits as spec i previous step.
    next header starts now, repeat
    """
    binary_message = base_message[:]
    version_total = 0
    while len(binary_message) > 0:
        head = binary_message[:6]
        version = int(head[:3], 2)
        version_total += version
        type_id = int(head[3:], 2)
        binary_message = binary_message[6:]
        if type_id == 4:
            # read_literal() when value is needed
            # for now, just skip correct amount of bits
            pass
        else:
            # read_operator() when doing operations (this should be recusive for operators in operators)
            # for now, just skip correct amount of bits
            pass
    return version_total


def adv16_2():
    pass


def main():
    data = []
    with open("bits_data.txt") as f:
        data = f.readlines()
    f.close

    binary_string = ''
    for hex in data[0]:
        binary_string += str("{0:04b}".format(int(hex, 16)))

    print("part 1 - :", adv16_1(binary_string))
    print("part 2 - :", adv16_2())

if __name__ == '__main__':
    main()
