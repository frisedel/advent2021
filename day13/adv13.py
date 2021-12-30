#!/usr/bin/env python3

from typing import List, Tuple
from itertools import zip_longest

def fold_paper(paper: List[List[int]], fold: Tuple[str, int]):
    if fold[0] == 'x':
        return fold_x(paper, fold[1])
    else:
        return fold_y(paper, fold[1])

def fold_x(paper: List[List[int]], fold_at: int):
    folded_paper: List[List[int]] = []
    for line in paper:
        first = line[:fold_at]
        first.reverse()
        second = line[fold_at+1:]
        new_line = list(map(sum, zip_longest(first, second, fillvalue=0)))
        new_line.reverse()
        folded_paper.append(new_line)
    return folded_paper


def fold_y(paper: List[List[int]], fold_at: int):
    folded_paper: List[List[int]] = []
    first = paper[:fold_at]
    first.reverse()
    second = paper[fold_at+1:]

    long = first if len(first) >= len(second) else second
    short = second if len (first) >= len(second) else first

    for index in range(len(long)):
        try:
            new = list(map(sum, zip(long[index], short[index])))
            folded_paper.append(new)
        except:
            folded_paper.append(long[index])
    folded_paper.reverse()
    return folded_paper


def count_dots(paper: List[List[int]]) -> int:
    total = 0
    for line in paper:
        total += len(line) - line.count(0)
    return total


def adv13_1(paper: List[List[int]], folds: List[Tuple[str, int]]):
    folded_paper = fold_paper(paper, folds[0])
    return count_dots(folded_paper)


def adv13_2(paper: List[List[int]], folds: List[Tuple[str, int]]) -> str:
    folded_paper = paper[:]
    for fold in folds:
        folded_paper = fold_paper(folded_paper, fold)

    text_output = '\n'
    for line in folded_paper:
        new_line = ''
        for val in line:
            if val > 0:
                new_line += '# '
            else:
                new_line += '. '
        text_output += (new_line + '\n')
    return text_output

def construct_coordinates(paper_data: List[str]):
    return list(map(eval, paper_data))


def construct_paper(coordinates: List[Tuple[int, int]]) -> List[List[int]]:
    x_max = 0
    y_max = 0
    for coord in coordinates:
        if coord[0] > x_max:
            x_max = coord[0]
        if coord[1] > y_max:
            y_max = coord[1]

    paper = [[0 for x in range(x_max+1)] for y in range(y_max+1)]

    for x,y in coordinates:
        paper[y][x] +=1

    return paper


def extraxt_folds(instructions: List[str]) -> List[Tuple[str, int]]:
    folds = []
    for line in instructions:
        f = line.split()[-1].split('=')
        folds.append((f[0], int(f[1])))
    return folds


def main():
    paper_data = []
    with open("paper_data.txt") as f:
        paper_data = f.readlines()
    f.close

    dot_coordinates: List[Tuple[int, int]] = construct_coordinates(paper_data)
    paper = construct_paper(dot_coordinates)

    folding_data = []
    with open("fold_instructions.txt") as f:
        folding_data = f.readlines()
    f.close

    folds = extraxt_folds(folding_data)

    print("part 1 - Number of visible dots after first fold:", adv13_1(paper, folds))
    print("part 2 - Activation code for infrared thermal imaging camera system:", adv13_2(paper, folds))

if __name__ == '__main__':
    main()
