#!/usr/bin/env python3

from typing import List

opening_chars = ['(', '[', '{', '<']
closing_chars = [')', ']', '}', '>']

def find_closing(syntax_index: int, syntax_line: List[str]):
    depth = 0

    char = syntax_line[syntax_index]

    for next_char in range(syntax_index+1, len(syntax_line)):
        if syntax_line[next_char] in opening_chars:
            depth += 1
        else:
            depth -= 1
            if depth == 0 and opening_chars.index(char) == closing_chars.index(syntax_line[next_char]):
                return syntax_line[next_char]


def find_error(syntax_line: List[str]) -> str:
    for index in range(len(syntax_line)-1):
        if syntax_line[index] in opening_chars:
            closing = find_closing(index, syntax_line)
            if closing != None:
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

def adv10_2():
    pass

def main():
    input_data = []
    with open("syntax_input.txt") as f:
        input_data = f.readlines()
    f.close

    syntax_data:List[List[str]] = []
    for line in input_data:
        syntax_data.append(list(line.strip()))

    print("part 1 - Total syntax error score:", adv10_1(syntax_data))
    print("part 2 - :", adv10_2())

if __name__ == '__main__':
    main()
