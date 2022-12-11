from collections import deque
from test_input.test_data_day5 import test_crates
from day5.adv_5 import make_stacks

test_stacks = [deque(['Z', 'N']), deque(['M', 'C', 'D']), deque(['P'])]

def test_make_stacks():
    stacks = make_stacks(test_crates, 3)
    assert stacks == test_stacks