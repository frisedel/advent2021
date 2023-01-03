#!/usr/bin/env python3

from collections import namedtuple, deque
import copy
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
    for _ in range(20):
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

    inspections = [monkey.inspected_items for monkey in monkeys]
    inspections.sort(reverse=True)

    return inspections[0] * inspections[1]


def adv11_2(monkeys: List[Monkey], worry_modifier: int) -> int:
    for _ in range(10000):
        for monkey in monkeys:
            while monkey.items:
                item = monkey.items.popleft()
                b_value = int(monkey.operation_value) if monkey.operation_value != "old" else item
                new_wory_level = monkey.operation(item, b_value)
                monkey.inspected_items += 1
                if new_wory_level % monkey.test_value == 0:
                    monkeys[monkey.throws_to.true].items.append(new_wory_level % worry_modifier)
                else:
                    monkeys[monkey.throws_to.false].items.append(new_wory_level % worry_modifier)

    inspections = [monkey.inspected_items for monkey in monkeys]
    inspections.sort(reverse=True)

    return inspections[0] * inspections[1]


def parse_monkeys(monkey_data: List[str]):
    worry_modifier = 1
    monkeys: List[Monkey] = []
    for i in range(0, len(monkey_data), 7):
        number = int(list(monkey_data[i].split(" ")[1])[0])
        items = deque(int(x) for x in (monkey_data[i+1].split(": ")[1]).split(", "))
        operation = multiply if (monkey_data[i+2].split(" ")[-2]) == "*" else add
        operation_value = (monkey_data[i+2].split(" ")[-1])
        test_value = int(monkey_data[i+3].split(" ")[-1])
        worry_modifier *= test_value
        throws_to = Throws_to(int(monkey_data[i+4].split(" ")[-1]), int(monkey_data[i+5].split(" ")[-1]))

        monkeys.append(Monkey(number, items, operation, operation_value, test_value, throws_to))
    return monkeys, worry_modifier


def main():

    monkey_data: List[str] = []
    with open("monkey_data.txt") as f:
        monkey_data = f.read().splitlines()
    f.close()

    monkeys, worry_modifier = parse_monkeys(monkey_data)

    print("part 1 - Level of monkey business after 20 rounds:", adv11_1(copy.deepcopy(monkeys)))
    print("part 2 - Level of monkey business after 10000 rounds:", adv11_2(copy.deepcopy(monkeys), worry_modifier))


if __name__ == '__main__':
    main()
