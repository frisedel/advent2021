#!/usr/bin/env python3

from typing import List

from day6.adv6 import adv6_1, process_lantern_generations

lanterns_data: List[int] = [3,4,3,1,2]
lanterns_after_18: List[int] = [6,0,6,4,5,6,0,1,1,2,6,0,1,1,1,2,2,3,3,4,6,7,8,8,8,8]

def test_process_generations():
    lanterns = process_lantern_generations(lanterns_data, [], 18, 0)
    assert lanterns == lanterns_after_18
    assert len(lanterns) == 26

def test_adv6_1():
    number_of_lanterns = adv6_1(lanterns_data)
    assert number_of_lanterns == 5934