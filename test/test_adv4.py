#!/usr/bin/env python3

import pytest

from day4.adv4 import calculate_winning_score, create_boards, get_boards_for_next, get_numbers_for_next, let_the_squid_winn, get_numbers, get_first_winning_board

boards_data = ['22 13 17 11  0\n', ' 8  2 23  4 24\n', '21  9 14 16  7\n', ' 6 10  3 18  5\n', ' 1 12 20 15 19\n', '\n' ' 3 15  0  2 22\n', ' 9 18 13 17  5\n', '19  8  7 25 23\n', '20 11 10 24  4\n', '14 21 16 12  6\n', '\n', '14 21 17 24  4\n', '10 16 15  9 19\n', '18  8 23 26 20\n', '22 11 13  6  5\n', ' 2  0 12  3  7']
bingo_numbers = ['7', '4', '9', '5', '11', '17', '23', '2', '0', '14', '21', '24', '10', '16', '13', '6', '15', '25', '12', '22', '18', '20', '8', '19', '3', '26', '1']

def test_create_boards():
    boards = create_boards(boards_data)
    assert boards == [
        {'board num': 1, 'board': [
            [{'val': 22, 'found': False}, {'val': 13, 'found': False}, {'val': 17, 'found': False}, {'val': 11, 'found': False}, {'val': 0, 'found': False}],
            [{'val': 8, 'found': False}, {'val': 2, 'found': False}, {'val': 23, 'found': False}, {'val': 4, 'found': False}, {'val': 24, 'found': False}],
            [{'val': 21, 'found': False}, {'val': 9, 'found': False}, {'val': 14, 'found': False}, {'val': 16, 'found': False}, {'val': 7, 'found': False}],
            [{'val': 6, 'found': False}, {'val': 10, 'found': False}, {'val': 3, 'found': False}, {'val': 18, 'found': False}, {'val': 5, 'found': False}],
            [{'val': 1, 'found': False}, {'val': 12, 'found': False}, {'val': 20, 'found': False}, {'val': 15, 'found': False}, {'val': 19, 'found': False}]
        ]},
        {'board num': 2, 'board': [
            [{'val': 3, 'found': False}, {'val': 15, 'found': False}, {'val': 0, 'found': False}, {'val': 2, 'found': False}, {'val': 22, 'found': False}],
            [{'val': 9, 'found': False}, {'val': 18, 'found': False}, {'val': 13, 'found': False}, {'val': 17, 'found': False}, {'val': 5, 'found': False}],
            [{'val': 19, 'found': False}, {'val': 8, 'found': False}, {'val': 7, 'found': False}, {'val': 25, 'found': False}, {'val': 23, 'found': False}],
            [{'val': 20, 'found': False}, {'val': 11, 'found': False}, {'val': 10, 'found': False}, {'val': 24, 'found': False}, {'val': 4, 'found': False}],
            [{'val': 14, 'found': False}, {'val': 21, 'found': False}, {'val': 16, 'found': False}, {'val': 12, 'found': False}, {'val': 6, 'found': False}]
        ]},
        {'board num': 3, 'board': [
            [{'val': 14, 'found': False}, {'val': 21, 'found': False}, {'val': 17, 'found': False}, {'val': 24, 'found': False}, {'val': 4, 'found': False}],
            [{'val': 10, 'found': False}, {'val': 16, 'found': False}, {'val': 15, 'found': False}, {'val': 9, 'found': False}, {'val': 19, 'found': False}],
            [{'val': 18, 'found': False}, {'val': 8, 'found': False}, {'val': 23, 'found': False}, {'val': 26, 'found': False}, {'val': 20, 'found': False}],
            [{'val': 22, 'found': False}, {'val': 11, 'found': False}, {'val': 13, 'found': False}, {'val': 6, 'found': False}, {'val': 5, 'found': False}],
            [{'val': 2, 'found': False}, {'val': 0, 'found': False}, {'val': 12, 'found': False}, {'val': 3, 'found': False}, {'val': 7, 'found': False}]
        ]}
    ]

def test_get_numbers():
    numbers = get_numbers(bingo_numbers)
    assert numbers == [7, 4, 9, 5, 11, 17, 23, 2, 0, 14, 21, 24, 10, 16, 13, 6, 15, 25, 12, 22, 18, 20, 8, 19, 3, 26, 1]

def test_get_winning_board():
    boards = create_boards(boards_data)
    numbers = get_numbers(bingo_numbers)
    winning_board, last_number = get_first_winning_board(boards, numbers)
    assert (winning_board, last_number) == (3, 24)

def test_calculate_winning_score():
    boards = create_boards(boards_data)
    numbers = get_numbers(bingo_numbers)
    winning_board, last_number = get_first_winning_board(boards, numbers)
    score = calculate_winning_score(boards[winning_board-1], last_number)
    assert score == 4512


def test_get_numbers_for_next():
    numbers = get_numbers(bingo_numbers)
    numbers_for_next = get_numbers_for_next(numbers, 24)
    print(numbers_for_next)
    assert numbers_for_next == [7, 4, 9, 5, 11, 17, 23, 2, 0, 14, 21, 10, 16, 13, 6, 15, 25, 12, 22, 18, 20, 8, 19, 3, 26, 1]

def test_get_boards_for_next():
    boards = create_boards(boards_data)
    boards_for_next = get_boards_for_next(boards, 3)
    assert boards_for_next == [
        {'board num': 1, 'board': [
            [{'val': 22, 'found': False}, {'val': 13, 'found': False}, {'val': 17, 'found': False}, {'val': 11, 'found': False}, {'val': 0, 'found': False}],
            [{'val': 8, 'found': False}, {'val': 2, 'found': False}, {'val': 23, 'found': False}, {'val': 4, 'found': False}, {'val': 24, 'found': False}],
            [{'val': 21, 'found': False}, {'val': 9, 'found': False}, {'val': 14, 'found': False}, {'val': 16, 'found': False}, {'val': 7, 'found': False}],
            [{'val': 6, 'found': False}, {'val': 10, 'found': False}, {'val': 3, 'found': False}, {'val': 18, 'found': False}, {'val': 5, 'found': False}],
            [{'val': 1, 'found': False}, {'val': 12, 'found': False}, {'val': 20, 'found': False}, {'val': 15, 'found': False}, {'val': 19, 'found': False}]
        ]},
        {'board num': 2, 'board': [
            [{'val': 3, 'found': False}, {'val': 15, 'found': False}, {'val': 0, 'found': False}, {'val': 2, 'found': False}, {'val': 22, 'found': False}],
            [{'val': 9, 'found': False}, {'val': 18, 'found': False}, {'val': 13, 'found': False}, {'val': 17, 'found': False}, {'val': 5, 'found': False}],
            [{'val': 19, 'found': False}, {'val': 8, 'found': False}, {'val': 7, 'found': False}, {'val': 25, 'found': False}, {'val': 23, 'found': False}],
            [{'val': 20, 'found': False}, {'val': 11, 'found': False}, {'val': 10, 'found': False}, {'val': 24, 'found': False}, {'val': 4, 'found': False}],
            [{'val': 14, 'found': False}, {'val': 21, 'found': False}, {'val': 16, 'found': False}, {'val': 12, 'found': False}, {'val': 6, 'found': False}]
        ]}
    ]

def test_let_the_squid_winn():
    boards = create_boards(boards_data)
    numbers = get_numbers(bingo_numbers)
    last_winning_board, last_winning_number = let_the_squid_winn(boards, numbers)
    assert (last_winning_board, last_winning_number) == (2, 13)
    score = calculate_winning_score(boards[last_winning_board-1], last_winning_number)
    assert score == 1924