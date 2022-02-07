#!/usr/bin/env python3

from typing import List, Tuple
from copy import deepcopy
from day5.adv5 import adv5_1, adv5_2, convert_to_tuples, create_matrix, create_vent_lists, get_matrix_size, mark_diagonal_lines_in_matrix, mark_straight_lines_in_matrix, separate_directions, sort_diagonals, sort_stright_lists, split_diagonal, split_straight

vent_data = ["0,9 -> 5,9", "8,0 -> 0,8", "9,4 -> 3,4", "2,2 -> 2,1", "7,0 -> 7,4", "6,4 -> 2,0", "0,9 -> 2,9", "3,4 -> 1,4", "0,0 -> 8,8", "5,5 -> 8,2"]
vent_tuples: List[List[Tuple[int, int]]] = [[(0,9), (5,9)], [(8,0), (0,8)], [(9,4), (3,4)], [(2,2), (2,1)], [(7,0), (7,4)], [(6,4), (2,0)], [(0,9), (2,9)], [(3,4), (1,4)], [(0,0), (8,8)], [(5,5), (8,2)]]
straight_lines: List[List[Tuple[int, int]]] = [[(0,9), (5,9)], [(9,4), (3,4)], [(2,2), (2,1)], [(7,0), (7,4)], [(0,9), (2,9)], [(3,4), (1,4)]]
diagonal_lines: List[List[Tuple[int, int]]] = [[(8,0), (0,8)], [(6,4), (2,0)], [(0,0), (8,8)], [(5,5), (8,2)]]
sorted_diagonal: List[List[Tuple[int, int]]] = [[(0,8), (8,0)], [(2,0), (6,4)], [(0,0), (8,8)], [(5,5), (8,2)]]
vertical_vent_lines: List[List[Tuple[int, int]]] = [[(2,2), (2,1)], [(7,0), (7,4)]]
horizontal_vent_lines: List[List[Tuple[int, int]]] = [[(0,9), (5,9)], [(9,4), (3,4)], [(0,9), (2,9)], [(3,4), (1,4)]]

sorted_vertical = [[(2,1), (2,2)], [(7,0), (7,4)]]
sorted_horizontal = [[(0,9), (5,9)], [(3,4), (9,4)], [(0,9), (2,9)], [(1,4), (3,4)]]
out: List[List[Tuple[int, int]]] = [[(2,0), (6,4)], [(0,0), (8,8)]]
x_to_y: List[List[Tuple[int, int]]] = [[(0,8), (8,0)], [(5,5), (8,2)]]

base_matrix = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #0
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #1
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #2
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #3
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #4
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #5
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #6
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #7
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #8
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  #9
    #0  1  2  3  4  5  6  7  8  9
]

def test_tuples():
    data = convert_to_tuples(vent_data)
    assert data == vent_tuples

def test_separate_directions():
    straight, diagonal = separate_directions(vent_tuples)
    assert straight == straight_lines
    assert diagonal == diagonal_lines

def test_split_straight_list():
    vertical, horizontal = split_straight(straight_lines)
    assert vertical == vertical_vent_lines
    assert horizontal == horizontal_vent_lines

def test_sort_straight_lists():
    local_vertical = vertical_vent_lines
    local_horizontal = horizontal_vent_lines
    sort_stright_lists(local_vertical, local_horizontal)
    assert local_vertical == sorted_vertical
    assert local_horizontal == sorted_horizontal

def test_sort_diagonals():
    local_diagonal = diagonal_lines
    sort_diagonals(local_diagonal)
    assert local_diagonal == sorted_diagonal

def test_split_diagonals():
    local_out, local_x_to_y = split_diagonal(sorted_diagonal)
    assert local_out == out
    assert local_x_to_y == x_to_y

def test_create_vent_lists():
    vertical, horizontal, local_out, local_x_to_y = create_vent_lists(vent_tuples)
    assert vertical == sorted_vertical
    assert horizontal == sorted_horizontal
    assert local_out == out
    assert local_x_to_y == x_to_y

def test_max_matrix():
    matrix_size = get_matrix_size(vent_tuples)
    assert matrix_size == 10

def test_create_matrix():
    matrix = create_matrix(get_matrix_size(vent_tuples))
    assert matrix == base_matrix

def test_mark_straight_in_matrix():
    local_matrix = deepcopy(base_matrix)
    mark_straight_lines_in_matrix(sorted_vertical, sorted_horizontal, local_matrix)
    assert local_matrix == [
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0], #0
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0], #1
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0], #2
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0], #3
    [0, 1, 1, 2, 1, 1, 1, 2, 1, 1], #4
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #5
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #6
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #7
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #8
    [2, 2, 2, 1, 1, 1, 0, 0, 0, 0]  #9
    #0  1  2  3  4  5  6  7  8  9
]

def test_mark_diagonal():
    local_matrix = deepcopy(base_matrix)
    mark_diagonal_lines_in_matrix(out, x_to_y, local_matrix)
    assert local_matrix == [
    [1, 0, 1, 0, 0, 0, 0, 0, 1, 0], #0
    [0, 1, 0, 1, 0, 0, 0, 1, 0, 0], #1
    [0, 0, 1, 0, 1, 0, 1, 0, 1, 0], #2
    [0, 0, 0, 1, 0, 2, 0, 1, 0, 0], #3
    [0, 0, 0, 0, 2, 0, 2, 0, 0, 0], #4
    [0, 0, 0, 1, 0, 2, 0, 0, 0, 0], #5
    [0, 0, 1, 0, 0, 0, 1, 0, 0, 0], #6
    [0, 1, 0, 0, 0, 0, 0, 1, 0, 0], #7
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 0], #8
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  #9
    #0  1  2  3  4  5  6  7  8  9
]

def test_adv5_1():
    local_matrix = deepcopy(base_matrix)
    vent_count = adv5_1(sorted_vertical, sorted_horizontal, local_matrix)
    assert vent_count == 5

def test_adv52():
    local_matrix = deepcopy(base_matrix)
    adv5_1(sorted_vertical, sorted_horizontal, local_matrix)
    vent_count = adv5_2(out, x_to_y, local_matrix)
    assert vent_count == 12