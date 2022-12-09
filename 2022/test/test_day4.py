from day4.adv_4 import adv4_1, create_pairs, fully_contains
from test_input.test_data_day4 import test_assignments

test_pair = [[(2,4), (6,8)]]

def test_create_pair():
    pair = create_pairs([test_assignments[0]])
    assert pair == test_pair

def test_fully_contains():
    pair0 = create_pairs([test_assignments[0]])[0]
    fully_contains0 = fully_contains(pair0)
    assert fully_contains0 == False

    pair3 = create_pairs([test_assignments[3]])[0]
    fully_contains3 = fully_contains(pair3)
    assert fully_contains3 == True

def test_adv4_1():
    pairs = create_pairs(test_assignments)
    count = adv4_1(pairs)
    assert count == 2