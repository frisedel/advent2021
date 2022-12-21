from day9.adv_9 import adv9_1, adv9_2, extract_movements
from test_input.test_data_day9 import test_rope_moves, test_rope_moves_large

def test_adv9_1():
    test_moves = extract_movements(test_rope_moves)
    count = adv9_1(test_moves)
    assert count == 13

def test_adv9_2():
    test_moves = extract_movements(test_rope_moves)
    count = adv9_2(test_moves)
    assert count == 1

    test_moves_large = extract_movements(test_rope_moves_large)
    count_large = adv9_2(test_moves_large)
    assert count_large == 36