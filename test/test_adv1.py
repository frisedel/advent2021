#!/usr/bin/env python3

from day1.adv1 import adv1_1, adv1_2

sonar_data = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

def test_adv1_1():
    numbers_increased = adv1_1(sonar_data)
    assert numbers_increased == 7

def test_adv1_2():
    blocks_increased = adv1_2(sonar_data)
    assert blocks_increased == 5