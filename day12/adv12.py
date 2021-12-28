#!/usr/bin/env python3

from typing import Dict, List
from collections import Counter
from copy import deepcopy

def visited_a_small_twice(path: List[str]) -> bool:
    small_caves = [cave for cave in path if cave.islower()]
    return len([cave for cave, v in Counter(small_caves).items() if v > 1]) > 0

def navigate_caves(cave_graph: Dict[str, List[str]], paths: List[List[str]], path: List[str], cave: str, use_double_visit: bool = False):
    path.append(cave)
    if cave == "end":
        paths.append(path)
        return
    for neighbour in cave_graph[cave]:
        if neighbour == "start":
            continue
        if neighbour.islower() and neighbour in path:
            if use_double_visit and not visited_a_small_twice(path):
                navigate_caves(cave_graph, paths, path[:], neighbour, use_double_visit)
            else:
                continue
        else:
            navigate_caves(cave_graph, paths, path[:], neighbour, use_double_visit)


def trim_graph(cave_graph: Dict[str, List[str]]):
    to_remove: List[str] = []
    for node in cave_graph:
        if len(cave_graph[node]) == 0:
            to_remove.append(node)
        if node != 'start' and node != 'end' and len(cave_graph[node]) == 1 and cave_graph[node][0].islower():
            to_remove.append(node)
    for dead_end in to_remove:
        del cave_graph[dead_end]
        for node in cave_graph:
            if dead_end in cave_graph[node]:
                cave_graph[node].remove(dead_end)


def adv12_1(cave_graph: Dict[str, List[str]]):
    trimmed = deepcopy(cave_graph)
    trim_graph(trimmed)
    paths: List[List[str]] = []
    navigate_caves(trimmed, paths, [], "start")
    return len(paths)


def adv12_2(cave_graph: Dict[str, List[str]]):
    paths: List[List[str]] = []
    navigate_caves(cave_graph, paths, [], "start", True)
    return len(paths)


def main():
    data = []
    with open("tree_data.txt") as f:
        data = f.readlines()
    f.close

    cave_graph: Dict[str, List[str]] = {}
    for line in data:
        node_conection = line.strip().split('-')
        if node_conection[0] not in cave_graph.keys():
            cave_graph[node_conection[0]] = []
        if node_conection[1] not in cave_graph.keys():
            cave_graph[node_conection[1]] = []

        cave_graph[node_conection[1]].append(node_conection[0])
        cave_graph[node_conection[0]].append(node_conection[1])



    print("part 1 - Number of paths to end:", adv12_1(cave_graph))
    print("part 2 - Number of paths to end with one double visit:", adv12_2(cave_graph))

if __name__ == '__main__':
    main()
