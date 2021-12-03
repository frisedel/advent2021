#!/usr/bin/env python3

import pytest

from day3.adv3 import adv3_1, convert_binary, get_rates, adv3_2, calc_common_bits, co2_scrubber_rating, oxygen_generator_rating

def test_adv3_1():
    diagnostic_codes = ["00100", "11110", "10110", "10111", "10101", "01111", "00111", "11100", "10000", "11001", "00010", "01010"]

    power_consumption = adv3_1(diagnostic_codes)
    assert power_consumption == 198

def test_get_rates():
    diagnostic_codes = ["00100", "11110", "10110", "10111", "10101", "01111", "00111", "11100", "10000", "11001", "00010", "01010"]

    gamma, epislon = get_rates(diagnostic_codes)
    assert gamma == "10110"
    assert epislon == "01001"

def test_convert_binary():
    gamma = convert_binary("10110")
    epislon = convert_binary("01001")

    assert gamma == 22
    assert epislon == 9

def test_adv3_2():
    diagnostic_codes = ["00100", "11110", "10110", "10111", "10101", "01111", "00111", "11100", "10000", "11001", "00010", "01010"]

    life_support_rating = adv3_2(diagnostic_codes)
    assert life_support_rating == 230

def test_oxygen_generator_rating():
    diagnostic_codes = ["00100", "11110", "10110", "10111", "10101", "01111", "00111", "11100", "10000", "11001", "00010", "01010"]

    oxygen = oxygen_generator_rating(diagnostic_codes, 0)
    assert oxygen == 23

def test_co2_scrubber_rating():
    diagnostic_codes = ["00100", "11110", "10110", "10111", "10101", "01111", "00111", "11100", "10000", "11001", "00010", "01010"]

    oxygen = co2_scrubber_rating(diagnostic_codes, 0)
    assert oxygen == 10

def test_calc_common():
    diagnostic_codes = ["00100", "11110", "10110", "10111", "10101", "01111", "00111", "11100", "10000", "11001", "00010", "01010"]

    common_first_bit_o2 = calc_common_bits(diagnostic_codes, 0, "o2")
    assert common_first_bit_o2 == 1

    common_first_bit_co2 = calc_common_bits(diagnostic_codes, 0, "co2")
    assert common_first_bit_co2 == 0