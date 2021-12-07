#!/usr/bin/env python3

from typing import List, Tuple
from day5.adv5 import adv5_1, convert_to_tuples, create_matrix, create_vent_lists, get_matrix_size, mark_in_matrix, max_from_list, separate_directions, sort_stright_lists, split_straight

vent_data = ["0,9 -> 5,9", "8,0 -> 0,8", "9,4 -> 3,4", "2,2 -> 2,1", "7,0 -> 7,4", "6,4 -> 2,0", "0,9 -> 2,9", "3,4 -> 1,4", "0,0 -> 8,8", "5,5 -> 8,2"]
vent_tuples: List[List[Tuple[int, int]]] = [[(0,9), (5,9)], [(8,0), (0,8)], [(9,4), (3,4)], [(2,2), (2,1)], [(7,0), (7,4)], [(6,4), (2,0)], [(0,9), (2,9)], [(3,4), (1,4)], [(0,0), (8,8)], [(5,5), (8,2)]]
straight_lines: List[List[Tuple[int, int]]] = [[(0,9), (5,9)], [(9,4), (3,4)], [(2,2), (2,1)], [(7,0), (7,4)], [(0,9), (2,9)], [(3,4), (1,4)]]
#diagonal_lines = []
vertical_vent_lines: List[List[Tuple[int, int]]] = [[(2,2), (2,1)], [(7,0), (7,4)]]
horizontal_vent_lines: List[List[Tuple[int, int]]] = [[(0,9), (5,9)], [(9,4), (3,4)], [(0,9), (2,9)], [(3,4), (1,4)]]
sorted_vertical = [[(2,1), (2,2)], [(7,0), (7,4)]]
sorted_horizontal = [[(0,9), (5,9)], [(3,4), (9,4)], [(0,9), (2,9)], [(1,4), (3,4)]]
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
    #assert diagonal === diagonal_lines

def test_split_list():
    vertical, horizontal = split_straight(straight_lines)
    assert vertical == vertical_vent_lines
    assert horizontal == horizontal_vent_lines

def test_sort_lists():
    local_vertical = vertical_vent_lines
    local_horizontal = horizontal_vent_lines
    sort_stright_lists(local_vertical, local_horizontal)
    assert local_vertical == sorted_vertical
    assert local_horizontal == sorted_horizontal

def test_create_vent_lists():
    vertical, horizontal = create_vent_lists(vent_data)
    assert vertical == sorted_vertical
    assert horizontal == sorted_horizontal

def test_max_from_list():
    vertical_max = max_from_list(sorted_vertical)
    horizontal_max = max_from_list(sorted_horizontal)
    assert vertical_max == 7
    assert horizontal_max == 9

def test_max_matrix():
    matrix_size = get_matrix_size(sorted_vertical, sorted_horizontal)
    assert matrix_size == 10

def test_create_matrix():
    matrix = create_matrix(get_matrix_size(sorted_vertical, sorted_horizontal))
    assert matrix == base_matrix

def test_mark_in_matrix():
    local_matrix = base_matrix
    mark_in_matrix(sorted_vertical, sorted_horizontal, local_matrix)
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

def test_adv5_1():
    vent_count = adv5_1(vent_data)
    assert vent_count == 5