from day9.adv_9 import adv9_1, adv9_2, extract_movements
from test_input.test_data_day9 import test_rope_moves

def test_adv9_1():
    test_moves = extract_movements(test_rope_moves)
    count = adv9_1(test_moves)
    assert count == 13

def test_adv9_2():
    test_moves = extract_movements(test_rope_moves)
    count = adv9_2(test_moves)
    assert count == 9