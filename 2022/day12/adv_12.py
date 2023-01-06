#!/usr/bin/env python3

from typing import Dict, List, Tuple
from math import pow, sqrt


class Node:
    def __init__(self, node_id: str, x: int, y: int, height: int):
        self.node_id = node_id
        self.x = x
        self.y = y
        self.height = height
        self.neighbours: List[Node] = []


def horistic(next_node: Node, stop_node: Node):
    dX = pow((next_node.x - stop_node.x), 2)
    dY = pow((next_node.y - stop_node.y), 2)
    return sqrt(dX + dY)


def best_node(frontier: List[Node], stop_node: Node, cost_to_node: Dict[Node, int]) -> Node:
    score = {}
    for node in frontier:
        score[node] = (cost_to_node[node] + node.height + horistic(node, stop_node))
    return min(frontier, key=lambda x: score[x])


def reconstruct_path(cameFrom, start_node: Node, stop_node: Node) -> List[Node]:
    path = []
    node = stop_node
    while True:
        if node == start_node:
            path.append(node)
            path.reverse()
            return path
        else:
            path.append(node)
            node = cameFrom[node]


def a_star (start_id: str, stop_id: str, topology_map: Dict[int, Node]) -> List[Node]:
    start_node: Node = topology_map[start_id]
    stop_node: Node = topology_map[stop_id]
    frontier: List[Node] = [start_node]
    cost_to_node: Dict[Node, int] = {start_node: 0}
    came_from = {}
    visited: List[Node] = []

    while True:
        if not frontier:
            return False
        current = best_node(frontier, stop_node, cost_to_node)
        visited.append(current)
        frontier.remove(current)
        if current == stop_node:
            return reconstruct_path(came_from, start_node, stop_node)
        else:
            for next_node in current.neighbours:
                if (next_node not in visited) and (next_node not in frontier):
                    frontier.append(next_node)
                    came_from[next_node] = current
                    cost_to_node[next_node] = cost_to_node[current] + next_node.height
                if next_node in visited:
                    if (cost_to_node[current] + next_node.height) < cost_to_node[next_node]:
                        came_from[next_node] = current
                        cost_to_node[next_node] = cost_to_node[current] + next_node.height
                        frontier.append(next_node)
                        visited.remove(next_node)
                if next_node in frontier:
                    if (cost_to_node[current] + next_node.height) < cost_to_node[next_node]:
                        came_from[next_node] = current
                        cost_to_node[next_node] = cost_to_node[current] + next_node.height


def adv12_1(topology_map: Dict[str, Node], start_node: str, stop_node: str):
    reconstructed_path = a_star(start_node, stop_node, topology_map)
    return len(reconstructed_path) - 1


def adv12_2(topology_map: Dict[str, Node], start_node: str, stop_node: str):
    path_lengths: List[int] = []
    path_lengths.append(len(a_star(start_node, stop_node, topology_map))-1)
    starts = [node.node_id for node in topology_map.values() if node.height == 1]
    for start in starts:
        path = a_star(start, stop_node, topology_map)
        if path:
            path_lengths.append(len(path)-1)
    return min(path_lengths)


def create_node_id(x: int, y: int):
    return ''.join([str(x), ':', str(y)])


def construct_node(x: int, y: int, topology_data: List[List[str]]) -> Node:
    return Node(create_node_id(x, y), x, y, ord(topology_data[y][x])-96)


def point_exist(x_y: Tuple[int, int], topology_data: List[List[int]]) -> bool:
    max_x = len(topology_data[0])-1
    max_y = len(topology_data)-1
    return 0 <= x_y[0] <= max_x and 0 <= x_y[1] <= max_y


def update_node_neighbours(node: Node, int_map: List[List[int]], dict_map: Dict[str, Node]):
    a = (node.x, node.y-1)
    b = (node.x, node.y+1)
    c = (node.x-1, node.y)
    d = (node.x+1, node.y)

    if point_exist(a, int_map) and dict_map[f"{a[0]}:{a[1]}"].height < node.height + 2:
        node.neighbours.append(dict_map[create_node_id(a[0], a[1])])
    if point_exist(b, int_map) and dict_map[f"{b[0]}:{b[1]}"].height < node.height + 2:
        node.neighbours.append(dict_map[create_node_id(b[0], b[1])])
    if point_exist(c, int_map) and dict_map[f"{c[0]}:{c[1]}"].height < node.height + 2:
        node.neighbours.append(dict_map[create_node_id(c[0], c[1])])
    if point_exist(d, int_map) and dict_map[f"{d[0]}:{d[1]}"].height < node.height + 2:
        node.neighbours.append(dict_map[create_node_id(d[0], d[1])])


def create_map(topology_data: List[List[str]]):
    topology_dict: Dict[str, Node] = {}
    start_node: str = None
    stop_node: str = None

    for y in range(len(topology_data)):
        for x in range(len(topology_data[0])):
            if topology_data[y][x] == "S":
                start_node = create_node_id(x, y)
            if topology_data[y][x] == "E":
                stop_node = create_node_id(x, y)
            node = construct_node(x, y, topology_data)
            topology_dict[node.node_id] = node

    topology_dict[start_node].height = 0
    topology_dict[stop_node].height = ord('z')-95

    for node in topology_dict:
        update_node_neighbours(topology_dict[node], topology_data, topology_dict)

    return topology_dict, start_node, stop_node


def main():

    topology_data: List[List[str]] = []
    with open("topology_data.txt") as f:
        for line in f:
            topology_data.append([char for char in line.strip()])
    f.close()

    topology_map, start_node, stop_node = create_map(topology_data)

    print("part 1 - Steps required to reach top:", adv12_1(topology_map, start_node, stop_node))
    print("part 2 - Minimum steps for hiking trail:", adv12_2(topology_map, start_node, stop_node))


if __name__ == '__main__':
    main()
