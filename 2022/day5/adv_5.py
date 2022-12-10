#!/usr/bin/env python3

from collections import deque, namedtuple
from typing import Deque, List
import numpy as np

Order = namedtuple("Order", "amount source destination")


def adv5_1(crate_stacks: List[Deque], work_orders: List[Order]) -> str:
    for order in work_orders:
        for _ in range(order.amount):
            crate_stacks[order.destination].append(crate_stacks[order.source].pop())

    stack_tops: str = ""
    for stack in crate_stacks:
        stack_tops += stack.pop()

    return stack_tops


def adv5_2():

    return


def create_work_orders(order_data: List[str]):
    orders: List[Order] = []

    for line in order_data:
        work = line.split()
        orders.append(Order(int(work[1]), int(work[3])-1, int(work[5])-1))

    return orders


def make_stacks(crates_data: List[str]) -> List[Deque[str]]:
    crate_stacks: List[Deque[str]] = [deque() for _ in range(9)]

    crate_matrix = np.array([ list(x) for x in crates_data ]).transpose()
    crate_matrix = np.delete(crate_matrix, 0, 0)
    crate_matrix = np.delete(crate_matrix, -1, 0)

    for i in range(0, len(crate_matrix), 4):
        for char in np.flip(crate_matrix[i]):
            if char.isalpha():
                crate_stacks[i//4].append(char)

    return crate_stacks


def main():
    crates_data: List[str] = []
    work_data: List[Order] = []

    with open("crates.txt") as f:
        for line in f:
            line = line.strip()
            if "move " in line:
                work_data.append(line)
            else:
                crates_data.append(line)
    f.close()

    crate_stacks: List[Deque] = make_stacks(crates_data[:-2])
    work_orders: List[Order] = create_work_orders(work_data)

    print("part 1 - Top crates after move:", adv5_1(crate_stacks, work_orders))
    print("part 2 - :", adv5_2())


if __name__ == '__main__':
    main()
