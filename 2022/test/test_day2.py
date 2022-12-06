from day2.adv_2 import adv2_1, adv2_2, convert_strategy, get_corrected_points, get_points
from test_input.test_data_day2 import small_test

rounds_score = [8, 1, 6]
corrected_score = [4, 1, 7]

def test_get_points():
    points = get_points("AX")
    assert points == 4

def test_get_corrected_points():
    points = get_corrected_points("AX")
    assert points == 3

def test_convert_strategy():
   converted = convert_strategy(small_test, get_points)
   assert converted == rounds_score

   corrected = convert_strategy(small_test, get_corrected_points)
   assert corrected == corrected_score

def test_adv2_1():
    score = adv2_1(small_test)
    assert score == 15

def test_adv2_1():
    score = adv2_2(small_test)
    assert score == 12
