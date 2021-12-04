#!/usr/bin/env python3

from typing import Dict, List

def clean_boards(data: List[str]) -> List[str]:
    cleaned = list(filter(('\n').__ne__, data))
    splited: List[str] = []
    for string in cleaned:
        splited.append(string.split())
    return splited


def create_single_board(board: List[str]):
    int_board = []
    for line in board:
        line_data = list(line)
        int_data: List[Dict[int, bool]] = []
        for num in line_data:
            int_data.append({'val': int(num), 'found': False})
        int_board.append(int_data)
    return int_board


def create_boards(boards_data: List[str]):
    boards = []
    boards_data_cleaned = clean_boards(boards_data)
    data_length = len(boards_data_cleaned)

    for index in range(0, data_length-4, 5):
        board = create_single_board([boards_data_cleaned[index], boards_data_cleaned[index+1], boards_data_cleaned[index+2], boards_data_cleaned[index+3], boards_data_cleaned[index+4]])
        boards.append({'board num': len(boards)+1, 'board': board})
    return boards


def get_numbers(numbers: List[str]):
    int_numbers: List[int] = []
    for number in numbers:
        int_numbers.append(int(number))
    return int_numbers


def mark_numbers(boards: list, number: int):
    for board in boards:
        board_data = board['board']
        for line in board_data:
            for value in line:
                if value['val'] == number:
                    value['found'] = True


def get_first_winning_board(boards: list, numbers: List[int]):
    for number in numbers:
        mark_numbers(boards, number)
        for board in boards:
            board_data = board['board']
            for line in board_data:
                line_found = []
                for value in line:
                    line_found.append(value['found'])
                if all(line_found):
                    return (board['board num'], number)
            for i in range(5):
                column_found = []
                for j in range(5):
                    column_found.append(board_data[j][i]['found'])
                if all(column_found):
                    return (board['board num'], number)


def calculate_winning_score(board: list, last_number: int):
    board_data = board['board']
    not_called_value = 0
    for line in board_data:
        for value in line:
            if value['found'] == False:
                not_called_value += value['val']
    return not_called_value * last_number


def adv4_1(bingo_numbers: List[str], boards_data: List[str]):
    boards = create_boards(boards_data)
    numbers = get_numbers(bingo_numbers)
    winning_board, last_number = get_first_winning_board(boards, numbers)
    winning_index = winning_board-1
    score = calculate_winning_score(boards[winning_index], last_number)
    return score


def adv4_2():
    # recursive func like first winning score. go untill no winning board or last board
    # return all the way back
    # check if boars is winner, if is - go in again and calc with next number or remove from a list?
    pass

def main():
    bingo_numbers = []
    with open("numbers.txt") as f:
        data = f.read().strip()
        bingo_numbers = data.split(",")
    f.close()

    boards_data = []
    with open("boards.txt") as f:
        boards_data = f.readlines()
    f.close()

    print("part 1 - bingo score:", adv4_1(bingo_numbers, boards_data))


if __name__ == '__main__':
    main()
