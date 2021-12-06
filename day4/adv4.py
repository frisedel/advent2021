#!/usr/bin/env python3

from typing import Dict, List, Tuple

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


def get_first_winning_board(boards: list, numbers: List[int]) -> Tuple[int, int]:
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


def get_boards_for_next(boards: list, last_board: int):
    boards_for_next = []
    for board in boards:
        if board['board num'] != last_board:
            boards_for_next.append(board)

    return boards_for_next


def get_last_winning_board(boards: list, numbers: List[int], lates_board: int, latest_number: int) -> Tuple[int, int]:
    try:
        next_board, next_number = get_first_winning_board(boards, numbers)
    except:
        return (lates_board, latest_number)
    boards_for_next = get_boards_for_next(boards, next_board)
    return get_last_winning_board(boards_for_next, numbers, next_board, next_number)


def let_the_squid_winn(boards: list, numbers: List[int]):
    first_winning_board, first_winning_number = get_first_winning_board(boards, numbers)
    boards_for_next = get_boards_for_next(boards, first_winning_board)


    return get_last_winning_board(boards_for_next, numbers, first_winning_board, first_winning_number)


def adv4_2(bingo_boards: List[str], bingo_numbers: List[str]):
    boards = create_boards(bingo_boards)
    numbers = get_numbers(bingo_numbers)

    last_winning_board, last_winning_number = let_the_squid_winn(boards, numbers)
    last_index = last_winning_board-1
    last_score = calculate_winning_score(boards[last_index], last_winning_number)

    return last_score


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
    print("part 2 - last board score:", adv4_2(boards_data, bingo_numbers))


if __name__ == '__main__':
    main()
