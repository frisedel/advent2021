#!/usr/bin/env python3

from typing import Dict, List

from day6.adv6 import adv6_1, adv6_2, count_lanterns, process_lantern_generations

lanterns_data: List[int] = [3,4,3,1,2]
lanterns_after_18: Dict[int, int] = {0: 3, 1: 5, 2: 3, 3: 2, 4: 2, 5: 1, 6: 5, 7: 1, 8: 4}

def test_process_generations():
    lanterns = process_lantern_generations(lanterns_data, 18)
    print(lanterns)
    assert lanterns == lanterns_after_18

def test_count_lanterns():
    amount = count_lanterns(lanterns_after_18)
    assert amount == 26

def test_adv6_1():
    number_of_lanterns = adv6_1(lanterns_data)
    assert number_of_lanterns == 5934

def test_adv6_2():
    number_of_lanterns_256 = adv6_2(lanterns_data)
    assert number_of_lanterns_256 == 26984457539