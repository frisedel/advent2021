#!/usr/bin/env python3

def find_signal_start(datastream: str, signal_length: int) -> int:
    for i in range(signal_length, len(datastream)):
        signal = ""
        for j in range(1, signal_length + 1):
            signal += datastream[i-j]
        if len(set(signal)) == signal_length:
            return i
    raise Exception("FUCK YOU ELVES!")


def adv6_1(datastream: str) -> int:
    return find_signal_start(datastream, 4)


def adv6_2(datastream: str) -> int:
    return find_signal_start(datastream, 14)


def main():

    datastream = ""
    with open("datastream.txt") as f:
        datastream += f.read().rstrip()
    f.close()

    print("part 1 - Start of the first start-of-packet marker:", adv6_1(datastream))
    print("part 2 - Start of the first start-of-message marker:", adv6_2(datastream))


if __name__ == '__main__':
    main()

