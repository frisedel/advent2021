from day16.adv16 import adv16_1, adv16_2, get_literal_value, get_sub_packets, hex_to_bin
from test_input.test_data_day16 import lit_2021, lit_2021_bin, packet1_bin, packet_vs16, packet_1p2, packet_6t9, packet_min7, packet_max9, packet_5l15, packet_5ng15, packet_5ne15, packet_1p3_ne_2t2

def test_hex_to_bin():
    l_bin = hex_to_bin(lit_2021)
    assert l_bin == lit_2021_bin

def test_get_litteral_value():
    value, _ = get_literal_value(lit_2021_bin, 6)
    assert value == 2021

def test_get_sub_packets():
    packets, _ = get_sub_packets(packet1_bin, 6)
    assert packets[0].value == 10
    assert packets[1].value == 20

def test_adv16_1():
    bin_16 = hex_to_bin(packet_vs16)
    version_sum = adv16_1(bin_16)
    assert version_sum == 16

def test_adv16_2():
    bin_1p2 = hex_to_bin(packet_1p2)
    value_3 = adv16_2(bin_1p2)
    assert value_3 == 3

    bin_6t9 = hex_to_bin(packet_6t9)
    value_54 = adv16_2(bin_6t9)
    assert value_54 == 54

    bin_min7 = hex_to_bin(packet_min7)
    value_7 = adv16_2(bin_min7)
    assert value_7 == 7

    bin_max9 = hex_to_bin(packet_max9)
    value_9 = adv16_2(bin_max9)
    assert value_9 == 9

    bin_5l15 = hex_to_bin(packet_5l15)
    value_1 = adv16_2(bin_5l15)
    assert value_1 == 1

    bin_5ng15 = hex_to_bin(packet_5ng15)
    value_0 = adv16_2(bin_5ng15)
    assert value_0 == 0

    bin_5ne15 = hex_to_bin(packet_5ne15)
    value_0 = adv16_2(bin_5ne15)
    assert value_0 == 0

    bin_1p3_ne_2t2 = hex_to_bin(packet_1p3_ne_2t2)
    value_1 = adv16_2(bin_1p3_ne_2t2)
    assert value_1 == 1