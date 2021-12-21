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
    return None


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


def get_missing_chars(incomplete_line: List[str]) -> List[str]:
    missing_chars: List[str] = []
    for index in range(len(incomplete_line)):
        if incomplete_line[index] in open_close.keys():
            closing = find_closing(index, incomplete_line)
            if closing == None:
                opening = incomplete_line[index]
                missing_chars.append(open_close[opening])
    missing_chars.reverse()
    return missing_chars


def adv10_2(syntax_data: List[List[str]]):
    incomplete_syntax: List[List[str]] = []
    for line in syntax_data:
        error = find_error(line)
        if error == None:
            incomplete_syntax.append(line)

    missing_chars: List[List[str]] = []
    for line in incomplete_syntax:
        missing_chars.append(get_missing_chars(line))

    scores = []
    for missing in missing_chars:
        line_score = 0
        for char in missing:
            char_score = 0
            if char == ')':
                char_score = 1
            if char == ']':
                char_score = 2
            if char == '}':
                char_score = 3
            if char == '>':
                char_score = 4
            line_score = (line_score * 5) + char_score
        scores.append(line_score)
    scores.sort()
    return scores[int((len(scores)-1)/2)]


def main():
    input_data = []
    with open("syntax_input.txt") as f:
        input_data = f.readlines()
    f.close

    syntax_data:List[List[str]] = []
    for line in input_data:
        syntax_data.append(list(line.strip()))

    print("part 1 - Total syntax error score:", adv10_1(syntax_data))
    print("part 2 - Middle score of incomplete lines:", adv10_2(syntax_data))

if __name__ == '__main__':
    main()
