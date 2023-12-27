#!/usr/bin/env python3

from day3.adv_3 import adv3_1, adv3_2
from test_input.test_data_day3 import part_1

def test_adv3_1():
    sum_engine_schematics = adv3_1(part_1)
    assert sum_engine_schematics == 4361

# def test_adv3_2():
#     sum_power_sets = adv3_2(part_1)
#     assert sum_power_sets == 2286
