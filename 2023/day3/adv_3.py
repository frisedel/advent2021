#!/usr/bin/env python3

import re
from typing import List, Dict
from collections import namedtuple

Number = namedtuple("Number", "start stop value")
symbols = ['*', '%', '-', '#', '=', '@', '$', '/', '+', '&']

def adv3_1(schematics: List[str]) -> int:

    sum = 0

    for line_index, line in enumerate(schematics):
        line_len = len(line)-1
        def is_symbol(index: int) -> bool:
            try:
                char = line[index]
                return contains_symbol(char)
            except IndexError:
                return False
        
        def contains_symbol(string: str) -> bool:
            return any(ch in symbols for ch in string)

        numbers: List[Number] = []

        for match in re.finditer(r'\d+', line):
            numbers.append(Number(int(match.start()), int(match.end())-1, int(match.group())))

        for number in numbers:
            add_number = False
            if is_symbol(number.start-1) or is_symbol(number.stop+1):
                add_number = True

            if line_index > 0:
                above = schematics[line_index-1][number.start-1 if number.start > 0 else 0:number.stop+2 if number.stop < line_len else line_len]
                if contains_symbol(above):
                    add_number = True

            if line_index < len(schematics)-1:
                below = schematics[line_index+1][number.start-1 if number.start > 0 else 0:number.stop+2 if number.stop < line_len else line_len]
                if contains_symbol(below):
                    add_number = True
            
            if add_number:
                sum += number.value

    return sum

def adv3_2(schematics: List[str]) -> int:
    sum = 0

    return sum

def main():

    lines = []
    with open("engine_schematic.txt") as f:
        lines = f.read().splitlines()
    f.close()

    print("part 1 - sum of part numbers: ", adv3_1(lines))
    print("part 2 - sum of : ", adv3_2(lines))


if __name__ == '__main__':
    main()