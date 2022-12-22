from day10.adv_10 import adv10_1
from test_input.test_data_day10 import test_cycle_data_large

test_cycle_data_small = ["noop", "addx 3", "addx -5"]

def test_adv10_1():
    test_signal_strenghts = adv10_1(test_cycle_data_large)
    assert test_signal_strenghts == 13140
