#!/usr/bin/env python3

from day1.adv_1 import adv1_1, adv1_2
from test_input.test_data_day1 import part_1, part_2

def test_adv1_1():
    calibration_value = adv1_1(part_1)
    assert calibration_value == 142

def test_adv1_2():
    calibration_value = adv1_2(part_2)
    assert calibration_value == 281