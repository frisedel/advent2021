from day9.adv_9 import Movement, adv9_1, adv9_2, extract_movements, move_head, move_rope, move_tail
from test_input.test_data_day9 import test_rope_moves, test_rope_moves_large

def test_move_head():
    test_head = {"x": 0, "y": 0}
    test_move = Movement("R", 4)
    move_head(test_head, test_move)
    assert test_head == {"x": 4, "y": 0}

def test_move_tail():
    test_head = {"x": 4, "y": 0}
    test_tail = {"x": 0, "y": 0}
    test_tail_positions = ["0 0"]
    move_tail(test_head, test_tail, test_tail_positions)
    assert test_tail == {"x": 3, "y": 0}
    assert test_tail_positions == ["0 0", "1 0", "2 0", "3 0"]

def test_adv9_1():
    test_moves = extract_movements(test_rope_moves)
    count = adv9_1(test_moves)
    assert count == 13

def test_move_rope():
    test_head = {"x": 0, "y": 0}
    test_knot = {"x": 0, "y": 0}
    test_tail = {"x": 0, "y": 0}
    test_tail_positions = []
    test_move = Movement("R", 4)
    move_rope(test_move, [test_head, test_knot, test_tail], test_tail_positions)
    assert test_head == {"x": 4, "y": 0}
    assert test_tail == {"x": 2, "y": 0}
    test_set = set(test_tail_positions)
    assert len(test_set) == 3
    assert "0 0" in test_set and "1 0" in test_set and "2 0" in test_set

def test_adv9_2():
    test_moves = extract_movements(test_rope_moves)
    count = adv9_2(test_moves)
    assert count == 1

    test_moves_large = extract_movements(test_rope_moves_large)
    count_large = adv9_2(test_moves_large)
    assert count_large == 36