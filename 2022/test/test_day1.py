#!/usr/bin/env python3

from day1.adv_1 import adv1_1, adv1_2, convert_calorie_data, sum_calories
from test_input.test_data_day1 import test_calories

converted_calories = [[1000, 2000, 3000], [4000], [5000, 6000], [7000, 8000, 9000], [10000]]

summed_calories = [6000, 4000, 11000, 24000, 10000]


def test_convert_calories():
    converted = convert_calorie_data(test_calories)
    assert converted == converted_calories


def test_sum_calories():
    summed = sum_calories(converted_calories)
    assert summed == summed_calories


def test_adv1_1():
    max_calories = adv1_1(summed_calories)
    assert max_calories == 24000


def test_adv1_2():
    top_tree = adv1_2(summed_calories)
    assert top_tree == 45000
