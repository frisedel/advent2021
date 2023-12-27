#!/usr/bin/env python3

from day2.adv_2 import adv2_1, adv2_2
from test_input.test_data_day2 import part_1

def test_adv2_1():
    sum_legal_games = adv2_1(part_1)
    assert sum_legal_games == 8

def test_adv2_2():
    sum_power_sets = adv2_2(part_1)
    assert sum_power_sets == 2286
