from collections import deque
import copy
from day11.adv_11 import Monkey, Throws_to, add, adv11_1, adv11_2, multiply, parse_monkeys
from test_input.test_data_day11 import test_monkey_data

test_monkeys = [
    Monkey(0, deque([79, 98]), multiply, "19", 23, Throws_to(2, 3)),
    Monkey(1, deque([54, 65, 75, 74]), add, "6", 19, Throws_to(2, 0)),
    Monkey(2, deque([79, 60, 97]), multiply, "old", 13, Throws_to(1, 3)),
    Monkey(3, deque([74]), add, "3", 17, Throws_to(0, 1))
]

test_worry_modifier = 96577
test_monkey_business_20 = 10605
test_monkey_business_10000 = 2713310158

def test_parse_monkeys():
    monkeys, worry_modifier = parse_monkeys(test_monkey_data)
    for i, monkey in enumerate(monkeys):
        assert monkey.number == test_monkeys[i].number
        assert monkey.items == test_monkeys[i].items
        assert monkey.operation == test_monkeys[i].operation
        assert monkey.operation_value == test_monkeys[i].operation_value
        assert monkey.test_value == test_monkeys[i].test_value
        assert monkey.throws_to == test_monkeys[i].throws_to
    assert worry_modifier == test_worry_modifier

def test_adv11_1():
    test_monkey_business = adv11_1(copy.deepcopy(test_monkeys))
    assert test_monkey_business == test_monkey_business_20

def test_adv11_2():
    test_monkey_business = adv11_2(copy.deepcopy(test_monkeys), test_worry_modifier)
    assert test_monkey_business == test_monkey_business_10000