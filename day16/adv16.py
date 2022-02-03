#!/usr/bin/env python3
from typing import Tuple

def cut_str(transmission: str, cut_at: int) -> Tuple[str, str]:
    return transmission[:cut_at], transmission[cut_at:]


def cut_str_to_int(transmission: str, cut_at: int) -> Tuple[int, str]:
    val, transmission = cut_str(transmission, cut_at)
    return int(val, 2), transmission


def read_litteral(transmission: str) -> None:
    last_block = False
    # this should process the value for literal, but that is not needed for part 1
    # litteral_string = ''

    while not last_block:
        block, transmission = cut_str(transmission, 5)
        if block[0] == "0":
            last_block = True
            # add to litteral_string
        # else:
        #     add to litteral_string
    # convert litteral_string to int and return


def read_operator(transmission: str, version_total: int):
    operator_lenght_type, transmission = cut_str(transmission, 1)
    if operator_lenght_type == "0":
        message_lenght, transmission = cut_str_to_int(transmission, 15)
        operator_payload, transmission = cut_str(transmission, message_lenght)
        return decode_message(operator_payload, version_total)
    else:
        number_sub_packs, transmission = cut_str_to_int(transmission, 11)
        acc_total = 0
        for i in range(number_sub_packs):
            version_total += decode_message()


def decode_message(transmission: str, version_total: int):
    if len(transmission) == 0:
        return version_total

    header, transmission = cut_str(transmission, 6)
    version_total += int(header[:3], 2)
    type_id = int(header[3:6], 2)

    if type_id == 4:
        read_litteral(transmission)
    else:
        read_operator(transmission, version_total)
    decode_message(transmission, version_total)


def adv16_1(base_message: str):
    binary_message = base_message[:]
    version_total = 0
    # while len(binary_message) > 0:
    #     print(version_total)
    #     head = binary_message[:6]
    #     version = int(head[:3], 2)
    #     version_total += version
    #     # print("type_id:", head[3:])
    #     type_id = int(head[3:], 2)
    #     binary_message = binary_message[6:]
    #     if type_id == 4:
    #         # read_literal() when value is needed
    #         # for now, just skip correct amount of bits
    #         pass
    #     else:
    #         # read_operator() when doing operations (this should be recusive for operators in operators)
    #         # for now, just skip correct amount of bits
    #         pass
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
