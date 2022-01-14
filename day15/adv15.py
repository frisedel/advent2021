#!/usr/bin/env python3

from math import pow, sqrt
from typing import Dict, List, Tuple

class Node:
    def __init__(self, nodeID: str, x: int, y: int, value: int):
        self.nodeID = nodeID
        self.x = x
        self.y = y
        self.value = value
        self.neighbours: List[Node] = []


def horistic(next_node: Node, stop_node: Node):
    dX = pow((next_node.x - stop_node.x), 2)
    dY = pow((next_node.y - stop_node.y), 2)
    return sqrt(dX + dY)


def best_node(frontier: List[Node], stop_node, cost_to_node) -> Node:
    score = {}
    for obj in frontier:
        score[obj] = (cost_to_node[obj]+horistic(obj, stop_node))
    return min(frontier, key=lambda x: score[x])


def reconstruct_path(cameFrom, startNode, stopNode):
    path = []
    node = stopNode
    while True:
        if node == startNode:
            path.append(node)
            path.reverse()
            return path
        else:
            path.append(node)
            node = cameFrom[node]


def a_star (start_ID: str, end_ID: str, map_2d: Dict[int, Node]) -> List[Node]:
    start_node = map_2d[start_ID]
    stop_node = map_2d[end_ID]
    frontier = [start_node]
    cost_to_node = {start_node: 0}
    came_from = {}
    visited = []

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
                    cost_to_node[next_node] = cost_to_node[current] + horistic(current, next_node)
                if next_node in visited:
                    if (cost_to_node[current] + horistic(current, next_node)) < cost_to_node[next_node]:
                        came_from[next_node] = current
                        cost_to_node[next_node] = cost_to_node[current] + horistic(current, next_node)
                        frontier.append(next_node)
                        visited.remove(next_node)
                if next_node in frontier:
                    if (cost_to_node[current] + horistic(current, next_node)) < cost_to_node[next_node]:
                        came_from[next_node] = current
                        cost_to_node[next_node] = cost_to_node[current] + horistic(current, next_node)


def adv15_1(dict_map: Dict[int, Node], int_map: List[List[int]]):
    end_node = ''.join([str(len(int_map[0])-1), ':', str(len(int_map)-1)])
    reconstructed_path = a_star('0:0', end_node, dict_map)
    tot = 0
    if reconstructed_path:
        for node in reconstructed_path:
            print(node.nodeID, node.value)
            tot += node.value
    print(tot)
    """
    use A* to find optimal path
    total cost to next node/number should be the cost to go to that node plus distance to end where the latter is the heuristic value. distance is eiter straight line or steps
    possibly check frontier every loop for end before taking the one with the minimal cost
    """
    pass


def adv15_2():
    pass


def construct_node(x: int, y: int, map_2d: List[List[int]]) -> Node:
    nodeID = ''.join([str(x), ':', str(y)])
    return Node(nodeID, x, y, map_2d[y][x])


def point_exist(x_y: Tuple[int, int], int_map: List[List[int]]) -> bool:
    max_x = len(int_map[0])-1
    max_y = len(int_map)-1
    return 0 <= x_y[0] <= max_x and 0 <= x_y[1] <= max_y


def update_node_neighbours(node: Node, int_map: List[List[int]], dict_map: Dict[str, Node]):
    #   [.....]
    #   [--a--]
    #   [-cPd-]
    #   [--b--]
    #   [.....]

    a = (node.x, node.y-1)
    b = (node.x, node.y+1)
    c = (node.x-1, node.y)
    d = (node.x+1, node.y)

    exists: List[Tuple[int, int]] = []
    if point_exist(a, int_map):
        exists.append(a)
    if point_exist(b, int_map):
        exists.append(b)
    if point_exist(c, int_map):
        exists.append(c)
    if point_exist(d, int_map):
        exists.append(d)

    neighbours: List[Node] = []
    for point in exists:
        for neighbour_node in dict_map:
            if dict_map[neighbour_node].x == point[0] and dict_map[neighbour_node].y == point[1]:
                neighbours.append(dict_map[neighbour_node])

    node.neighbours.extend(neighbours)


def main():
    data = []
    with open("map_data_small.txt") as f:
        data = f.readlines()
    f.close

    int_map: List[List[int]] = []
    for line in data:
        row = []
        for value in line.strip():
            row.append(int(value))
        int_map.append(row)

    dict_map: Dict[int, Node] = {}
    for y in range(len(data)):
        for x in range(len(line)):
            node = construct_node(x, y, int_map)
            dict_map[node.nodeID] = node

    for node in dict_map:
        update_node_neighbours(dict_map[node], int_map, dict_map)

    print("part 1 - Cost for path with lowest risk:", adv15_1(dict_map, int_map))
    print("part 2 - :", adv15_2())

if __name__ == '__main__':
    main()
