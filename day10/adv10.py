#!/usr/bin/env python3

from typing import List

open_close = {'(': ')', '[': ']', '{': '}', '<': '>'}

def find_closing(syntax_index: int, syntax_line: List[str]):
    depth = 0
    for next_char in range(syntax_index, len(syntax_line)):
        if syntax_line[next_char] in open_close.keys():
            depth += 1
        else:
            depth -= 1
            if depth == 0:
                return syntax_line[next_char]


def find_error(syntax_line: List[str]) -> str:
    for index in range(len(syntax_line)):
        if syntax_line[index] in open_close.keys():
            opening = syntax_line[index]
            closing = find_closing(index, syntax_line)
            if closing != None and open_close[opening] != closing:
                return closing
    return '-'


def adv10_1(syntax_data: List[List[str]]):
    errors: List[str] = []
    for line in syntax_data:
        errors.append(find_error(line))
    total = 0
    for err in errors:
        if err == ')':
            total += 3
        if err == ']':
            total += 57
        if err == '}':
            total += 1197
        if err == '>':
            total += 25137
    return total


def adv10_2(syntax_data: List[List[str]]):
    incomplete_syntax: List[List[str]] = []
    for line in syntax_data:
        error = find_error(line)
        if error == '-':
            incomplete_syntax.append(line)

    # for line in incomplete_syntax:
    #     loop over again and where closing is None, insert what was expected
    # calculate score


def main():
    input_data = []
    with open("syntax_input.txt") as f:
        input_data = f.readlines()
    f.close

    syntax_data:List[List[str]] = []
    for line in input_data:
        syntax_data.append(list(line.strip()))

    print("part 1 - Total syntax error score:", adv10_1(syntax_data))
    print("part 2 - :", adv10_2(syntax_data))

if __name__ == '__main__':
    main()
