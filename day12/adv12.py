#!/usr/bin/env python3

from typing import Dict, List


def main():
    data = []
    with open("tree_data.txt") as f:
        data = f.readlines()
    f.close

    tree_graph: Dict[str, List[str]] = {}
    for line in data:
        node_conection = line.split('-')
        if node_conection[0] not in tree_graph.keys():
            tree_graph[node_conection[0]] = node_conection[1]
        else:
            tree_graph[node_conection[0]].append(node_conection[1])
        if node_conection[1] not in tree_graph.keys():
            tree_graph[node_conection[1]] = node_conection[0]
        else:
            tree_graph[node_conection[1]].append(node_conection[0])
    
    print(tree_graph)

    #print("part 1 - Number of flashes after 100 iterations:", adv11_1(octopus_data))
    #print("part 2 - Iteration when octopuses syncronize for the first time:", adv11_2(octopus_data))

if __name__ == '__main__':
    main()
