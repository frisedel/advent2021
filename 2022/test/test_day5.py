from collections import deque
from test_input.test_data_day5 import test_crates, test_order_data
from day5.adv_5 import Order, adv5_1, adv5_2, create_work_orders, make_stacks

test_stacks = [deque(['Z', 'N']), deque(['M', 'C', 'D']), deque(['P'])]
test_orders = [Order(amount=1, source=1, destination=0), Order(amount=3, source=0, destination=2), Order(amount=2, source=1, destination=0), Order(amount=1, source=0, destination=1)]

def test_make_stacks():
    stacks = make_stacks(test_crates, 3)
    assert stacks == test_stacks

def test_create_work_orders():
    orders = create_work_orders(test_order_data)
    assert orders == test_orders

def test_adv5_1():
    stacks = make_stacks(test_crates, 3)
    orders = create_work_orders(test_order_data)
    top_crates = adv5_1(stacks, orders)
    assert top_crates == "CMZ"

def test_adv5_2():
    stacks = make_stacks(test_crates, 3)
    orders = create_work_orders(test_order_data)
    top_crates = adv5_2(stacks, orders)
    assert top_crates == "MCD"