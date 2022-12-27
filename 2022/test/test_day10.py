from day10.adv_10 import adv10_1, adv10_2, check_cycle, write_CRT
from test_input.test_data_day10 import test_cycle_data_large

def test_check_cycle():
    test_signal_strengths = []
    check_cycle(2, 4, test_signal_strengths)
    assert test_signal_strengths == []

    check_cycle(60, 4, test_signal_strengths)
    assert test_signal_strengths == [240]

def test_adv10_1():
    test_signal_strenghts = adv10_1(test_cycle_data_large)
    assert test_signal_strenghts == 13140

def test_write_CRT():
    test_crt = [[" "] * 40 for _ in range(6)]
    empty_crt = [[" "] * 40 for _ in range(6)]
    write_CRT(2, 4, test_crt)
    assert test_crt == empty_crt

    expected_crt = [
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    ]
    write_CRT(2, 43, test_crt)
    print(test_crt)
    assert test_crt == expected_crt


def test_adv10_2():
    expected = [
        "##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ",
        "###   ###   ###   ###   ###   ###   ### ",
        "####    ####    ####    ####    ####    ",
        "#####     #####     #####     #####     ",
        "######      ######      ######      ####",
        "#######       #######       #######     "
    ]
    test_CRT = adv10_2(test_cycle_data_large)
    temp = []
    for line in test_CRT:
        temp.append("".join(line))
    assert temp == expected
