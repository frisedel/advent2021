#!/usr/bin/env python3

from typing import List, Tuple

def convert_to_tuples(vent_data: List[str]) -> List[List[Tuple[int, int]]]:
    converted_list: List[List[Tuple[int, int]]] = []
    for line in vent_data:
        splitted = line.split()
        part1 = splitted[0].split(",")
        part2 = splitted[2].split(",")
        int_data: List[Tuple[int, int]] = [(int(part1[0]), int(part1[1])), (int(part2[0]), int(part2[1]))]
        converted_list.append(int_data)
    return converted_list


def remove_diagonals(vent_data: List[List[Tuple[int, int]]]) -> List[List[Tuple[int, int]]]:
    straight_lines: List[List[Tuple[int, int]]] = []
    for vent_line in vent_data:
        if vent_line[0][0] == vent_line[1][0] or vent_line[0][1] == vent_line[1][1]:
            straight_lines.append(vent_line)
    return straight_lines


def split_list(vent_data: List[List[Tuple[int, int]]]):
    vertical = []
    horozontal = []
    for line in vent_data:
        if line[0][0] == line[1][0]:
            vertical.append(line)
        else:
            horozontal.append(line)
    return (vertical, horozontal)


def sort_lists(vertical: List[List[Tuple[int, int]]], horizontal: List[List[Tuple[int, int]]]):
    for points in vertical:
        if points[0][1] > points[1][1]:
            points[0], points[1] = points[1], points[0]
    for points in horizontal:
        if points[0][0] > points[1][0]:
            points[0], points[1] = points[1], points[0]



def create_vent_lists(vent_data: List[str]) -> Tuple[List[List[Tuple[int, int]]], List[List[Tuple[int, int]]]]:
    vent_data_tupels = convert_to_tuples(vent_data)
    data_straight = remove_diagonals(vent_data_tupels)
    vertical, horizontal = split_list(data_straight)
    sort_lists(vertical, horizontal)
    return (vertical, horizontal)


def max_from_list(data: List[List[Tuple[int, int]]]):
    max_value = 0
    for points in data:
        for point in points:
            point_max = max(point)
            if point_max > max_value:
                max_value = point_max
    return max_value


def get_matrix_size(vertical: List[List[Tuple[int, int]]], horizontal: List[List[Tuple[int, int]]]):
    max_vertical = max_from_list(vertical)
    max_horizontal = max_from_list(horizontal)
    return max(max_vertical, max_horizontal)


def mark_in_matrix(vertical: List[List[Tuple[int, int]]], horizontal: List[List[Tuple[int, int]]], vent_map: List[List[int]]):
    #take two lists
    #mark vertical vents by + 1 in cell
    #mark horizontal vents the same way
    pass


def count_dangerous_vents():
    #loop over matrix and count cells with value over 1
    #increase a value for each. go => for i in range(1000) for j range in range(1000) and check
    pass


def adv5_1(vent_data: List[str]):
    vertical, horizontal= create_vent_lists(vent_data)
    matrix_size = get_matrix_size(vertical, horizontal)
    vent_map = [[0 for j in range(matrix_size)] for i in range(matrix_size)]
    mark_in_matrix(vertical, horizontal, vent_map) # hope this works with reference
    #count vents - danger = count_dangerous_vents(vent_map)
    #return vent value
    pass


def main():
    #read alla lines
    vent_data = []
    with open("ventlines.txt") as f:
        vent_data = f.readlines()
    f.close

    print("part 1 - number of dangerous vents:", adv5_1(vent_data))
    pass


if __name__ == '__main__':
    main()
