from day11.adv_11 import parse_monkeys
from test_input.test_data_day11 import test_monkey_data

def test_parse_monkeys():
    monkeys = parse_monkeys(test_monkey_data)
    print(monkeys)
    assert False