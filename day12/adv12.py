#!/usr/bin/env python3

from typing import Dict, List

def adv12_1(tree_graph: Dict[str, List[str]]):
    print(tree_graph)
    number_of_paths = 0
    return number_of_paths


def adv12_2(tree_graph: Dict[str, List[str]]):
    pass


def trim_tree(tree_graph: Dict[str, List[str]]):
    to_remove: List[str] = []
    for node in tree_graph:
        if len(tree_graph[node]) == 0:
            to_remove.append(node)
        if node != 'start' and node != 'end' and len(tree_graph[node]) == 1 and tree_graph[node][0].islower():
            to_remove.append(node)
    for dead_end in to_remove:
        del tree_graph[dead_end]
        for node in tree_graph:
            if dead_end in tree_graph[node]:
                tree_graph[node].remove(dead_end)

def main():
    data = []
    with open("tree_data.txt") as f:
        data = f.readlines()
    f.close

    tree_graph: Dict[str, List[str]] = {}
    for line in data:
        node_conection = line.strip().split('-')
        if node_conection[0] not in tree_graph.keys():
            tree_graph[node_conection[0]] = []
        if node_conection[1] not in tree_graph.keys():
            tree_graph[node_conection[1]] = []

        tree_graph[node_conection[1]].append(node_conection[0])
        tree_graph[node_conection[0]].append(node_conection[1])

    trim_tree(tree_graph)

    print("part 1 - Number of paths to end:", adv12_1(tree_graph))
    print("part 2 - :", adv12_2(tree_graph))

if __name__ == '__main__':
    main()
