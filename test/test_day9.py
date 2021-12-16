from day9.adv9 import adv9_1, adv9_2

test_map = [
    [2, 1, 9, 9, 9, 4, 3, 2, 1 ,0],
    [3, 9, 8, 7, 8, 9, 4, 9, 2, 1],
    [9, 8, 5, 6, 7, 8, 9, 8, 9, 2],
    [8, 7, 6, 7, 8, 9, 6, 7, 8 ,9],
    [9, 8, 9, 9, 9, 6, 5, 6, 7 ,8]
]

def test_adv9_1():
    risk = adv9_1(test_map)
    assert risk == 15

def test_adv9_2():
    value = adv9_2(test_map)
    assert value == 1134