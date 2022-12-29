#!/usr/bin/env python3

from collections import namedtuple, deque
from typing import Callable, Deque, List

Throws_to = namedtuple("Throws_to", "true false")

class Monkey:
    def __init__(self, number: int, items: Deque[int], operation: Callable, operation_value: str, test_value: int, throws_to: Throws_to):
        self.number: int = number
        self.items: Deque[int] = items
        self.operation: Callable = operation
        self.operation_value: str = operation_value
        self.test_value: int = test_value
        self.throws_to: Throws_to = throws_to
        self.inspected_items: int = 0


def multiply(a: int, b: int):
    return a * b


def add(a: int, b: int):
    return a + b


def adv11_1(monkeys: List[Monkey]) -> int:
    for round in range(20):
        for monkey in monkeys:
            while monkey.items:
                item = monkey.items.popleft()
                b_value = int(monkey.operation_value) if monkey.operation_value != "old" else item
                new_wory_level = monkey.operation(item, b_value) // 3
                monkey.inspected_items += 1
                if new_wory_level % monkey.test_value == 0:
                    monkeys[monkey.throws_to.true].items.append(new_wory_level)
                else:
                    monkeys[monkey.throws_to.false].items.append(new_wory_level)
    for monkey in monkeys:
        print(monkey.inspected_items)
    return


def adv11_2(monkey_data: List[str]):
    return


def parse_monkeys(monkey_data: List[str]):
    monkeys: List[Monkey] = []
    for i in range(0, len(monkey_data), 7):
        number = int(list(monkey_data[i].split(" ")[1])[0])
        items = deque(int(x) for x in (monkey_data[i+1].split(": ")[1]).split(", "))
        operation = multiply if (monkey_data[i+2].split(" ")[-2]) == "*" else add
        operation_value = (monkey_data[i+2].split(" ")[-1])
        test_value = int(monkey_data[i+3].split(" ")[-1])
        throws_to = Throws_to(int(monkey_data[i+4].split(" ")[-1]), int(monkey_data[i+5].split(" ")[-1]))

        monkeys.append(Monkey(number, items, operation, operation_value, test_value, throws_to))
    return monkeys


def main():

    monkey_data: List[str] = []
    with open("mokey_data.txt") as f:
        monkey_data = f.read().splitlines()
    f.close()

    monkeys: List[Monkey] = parse_monkeys(monkey_data)

    print("part 1 - :", adv11_1(monkeys))
    print("part 2 - :", adv11_2(monkeys))


if __name__ == '__main__':
    main()
