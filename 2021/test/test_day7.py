#!/usr/bin/env python3

from typing import Dict, List

from day7.adv7 import adv7_1, adv7_2, calc_fuel_to_point, get_crab_map

crabs_data = [16,1,2,0,4,2,7,1,2,14]
crabs_gouped = {0:1, 1:2, 2:3, 4:1, 7:1, 14:1, 16:1}

def test_get_crab_map():
    crab_map = get_crab_map(crabs_data)
    assert crab_map == crabs_gouped

def test_calc_fuel_to_point():
    fuel_linear = calc_fuel_to_point(5, "linear")
    assert fuel_linear == 5

    fuel_increasing = calc_fuel_to_point(5, "increasing")
    assert fuel_increasing == 15

def test_adv7_1():
    crab_fuel_linear = adv7_1(crabs_data)
    assert crab_fuel_linear == 37

def test_adv7_2():
    crab_fuel_increase = adv7_2(crabs_data)
    assert crab_fuel_increase == 168