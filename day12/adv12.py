#!/usr/bin/env python3

from typing import Dict, List

def navigate_caves(cave_graph: Dict[str, List[str]], paths: List[List[str]], path: List[str], cave: str):
    path.append(cave)
    if cave == "end":
        paths.append(path)
        return
    for neighbour in cave_graph[cave]:
        if neighbour == "start" or neighbour.islower() and neighbour in path:
            continue
        else:
            navigate_caves(cave_graph, paths, path[:], neighbour)


def adv12_1(cave_graph: Dict[str, List[str]]):
    paths: List[List[str]] = []
    navigate_caves(cave_graph, paths, [], "start")
    return len(paths)


def adv12_2(cave_graph: Dict[str, List[str]]):
    pass


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

    trim_graph(cave_graph)

    print("part 1 - Number of paths to end:", adv12_1(cave_graph))
    print("part 2 - :", adv12_2(cave_graph))

if __name__ == '__main__':
    main()
