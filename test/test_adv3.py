#!/usr/bin/env python3

import pytest

from day3.adv3 import adv3_1

def test_adv3_1():
    diagnostic_codes = ["00100", "11110", "10110", "10111", "10101", "01111", "00111", "11100", "10000", "11001", "00010", "01010"]

    common = adv3_1(diagnostic_codes)
    assert common == 198