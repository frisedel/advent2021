#!/usr/bin/env python3

from day2.adv2 import adv2_1, adv2_2

commands = [("forward", 5), ("down", 5), ("forward", 8), ("up", 3), ("down", 8), ("forward", 2)]

def test_adv2_1():
    horizontal_times_depth = adv2_1(commands)
    assert horizontal_times_depth == 150

def test_adv2_2():
    position_with_aim = adv2_2(commands)
    assert position_with_aim == 900