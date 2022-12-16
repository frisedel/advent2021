#!/usr/bin/env python3

from typing import List
import numpy as np


def adv8_1(forest: np.ndarray) -> int:
    rows, columns = np.shape(forest)
    visability_count = 0
    for x in range(1, rows-1):
        for y in range(1, columns-1):
            tree = forest[x,y]
            if tree > np.max(forest[x,0:y]):
                visability_count += 1
            elif tree > np.max(forest[x,y+1:]):
                visability_count += 1
            elif tree > np.max(forest[0:x:,y]):
                visability_count += 1
            elif tree > np.max(forest[x+1:,y]):
                visability_count += 1

    return visability_count + (rows * 2) + ((columns - 2) * 2)


def directional_score(tree: int, forest_line: np.ndarray):
    score = 0
    for t in forest_line:
        score += 1
        if t >= tree:
            break
    return score


def adv8_2(forest: np.ndarray) -> int:
    rows, columns = np.shape(forest)
    scenic_scores: List[int] = []
    for x in range(rows):
        for y in range(columns):
            tree: int = forest[x,y]
            directional_scores = [0,0,0,0]

            directional_scores[0] = directional_score(tree, np.flip(forest[x,0:y]))
            directional_scores[1] = directional_score(tree, forest[x,y+1:])
            directional_scores[2] = directional_score(tree, np.flip(forest[0:x,y]))
            directional_scores[3] = directional_score(tree, forest[x+1:,y])

            scenic_scores.append(np.prod(directional_scores))

    return max(scenic_scores)


def map_forest(forest_data: List[str]) -> np.ndarray:
    return np.array([[int(tree) for tree in line] for line in forest_data])


def main():

    forest_data = []
    with open("reforestation_data.txt") as f:
        forest_data = f.read().splitlines()
    f.close()

    forest = map_forest(forest_data)

    print("part 1 - Amount of trees visible from outside the forest:", adv8_1(forest))
    print("part 2 - Highest scenic score:", adv8_2(forest))

if __name__ == '__main__':
    main()
