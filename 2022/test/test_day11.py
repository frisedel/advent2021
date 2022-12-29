from collections import deque
from day11.adv_11 import Monkey, Throws_to, add, adv11_1, multiply, parse_monkeys
from test_input.test_data_day11 import test_monkey_data

test_monkeys = [
    Monkey(0, deque([79, 98]), multiply, "19", 23, Throws_to(2, 3)),
    Monkey(1, deque([54, 65, 75, 74]), add, "6", 19, Throws_to(2, 0)),
    Monkey(2, deque([79, 60, 97]), multiply, "old", 13, Throws_to(1, 3)),
    Monkey(3, deque([74]), add, "3", 17, Throws_to(0, 1))
]

test_monkey_0_after_20 = deque([10, 12, 14, 26, 34])
test_monkey_1_after_20 = deque([245, 93, 53, 199, 115])

def test_parse_monkeys():
    monkeys = parse_monkeys(test_monkey_data)
    for i in range(len(monkeys)):
        assert monkeys[i].number == test_monkeys[i].number
        assert monkeys[i].items == test_monkeys[i].items
        assert monkeys[i].operation == test_monkeys[i].operation
        assert monkeys[i].operation_value == test_monkeys[i].operation_value
        assert monkeys[i].test_value == test_monkeys[i].test_value
        assert monkeys[i].throws_to == test_monkeys[i].throws_to


def test_adv11_1():
    test_monkey_business = adv11_1(test_monkeys)
    assert test_monkeys[0].items == test_monkey_0_after_20
    assert test_monkeys[1].items == test_monkey_1_after_20
    assert test_monkeys[0].inspected_items == 101
    assert test_monkeys[1].inspected_items == 95
    assert test_monkeys[2].inspected_items == 7
    assert test_monkeys[3].inspected_items == 105

    assert test_monkey_business == 10605