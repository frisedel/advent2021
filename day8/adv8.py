#!/usr/bin/env python3

from typing import List

def adv8_1(segment_data: List[str]):
    for code in segment_data:
        print(code)

def main():
    data = []
    with open("seven_segment.txt") as f:
        data = f.readlines()
    f.close

    segment_data: List[str] = []
    for code in data:
        segment_data.append(code.strip())


    print("part 1 - number of apperances:", adv8_1(segment_data))
    # print("part 2 - :", adv8_2())

if __name__ == '__main__':
    main()