#!/usr/bin/env python3

from typing import List

def get_bit_count(diag_codes: List[str]):
    number_of_bits = len(diag_codes[0])
    bits_count = [0.0] * number_of_bits

    for code in diag_codes:
        bits = list(code)
        for index in range(len(bits)):
            bits_count[index] += int(bits[index])
    return bits_count

def get_rates(diag_codes: List[str]):
    bits_count = get_bit_count(diag_codes)

    number_of_codes = len(diag_codes)
    gamma_rate = ""
    epsilon_rate = ""

    for bit in bits_count:
        bit_value = bit / number_of_codes
        if bit_value > 0.5:
            gamma_rate += str(1)
            epsilon_rate += str(0)
        else:
            gamma_rate += str(0)
            epsilon_rate += str(1)

    return gamma_rate, epsilon_rate

def adv3_1(diag_codes: List[str]):
    gamma_rate, epislon_rate = get_rates(diag_codes)
    gamma_value = int(gamma_rate, 2)
    epsilon_value = int(epislon_rate, 2)
    print("gamma:", gamma_value, "epsilon:", epsilon_value)

    return(gamma_value * epsilon_value)


def adv3_2(diag_codes: List[str]):
    print("h")

def main():
    lines = []
    with open("diagnostics.txt") as f:
        lines = f.read().splitlines()
    f.close()

    print("part 1:", adv3_1(lines))
    print("part 2:", adv3_2(lines))

if __name__ == '__main__':
    main()