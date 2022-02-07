from day12.adv12 import adv12_1, adv12_2, navigate_caves, visited_a_small_twice

test_caves_small = {'start': ['A', 'b'], 'A': ['start', 'b', 'c', 'end'], 'b': ['start', 'A', 'd', 'end'], 'c': ['A'], 'd': ['b']}

test_paths_small = [
    ['start', 'A', 'b', 'A', 'c', 'A', 'end'],
    ['start', 'A', 'b', 'A', 'end'],
    ['start', 'A', 'b', 'end'],
    ['start', 'A', 'c', 'A', 'b', 'A', 'end'],
    ['start', 'A', 'c', 'A', 'b', 'end'],
    ['start', 'A', 'c', 'A', 'end'],
    ['start', 'A', 'end'],
    ['start', 'b', 'A', 'c', 'A', 'end'],
    ['start', 'b', 'A', 'end'],
    ['start', 'b', 'end']
]

test_path_double_small = ['start', 'A', 'b', 'A', 'b', 'A', 'c', 'A', 'end']


def test_navigate_caves():
    paths = []
    navigate_caves(test_caves_small, paths, [], "start")
    assert paths == test_paths_small

def test_visit_small_twice():
    has_not = visited_a_small_twice(test_paths_small[0])
    assert has_not == False
    has = visited_a_small_twice(test_path_double_small)
    assert has == True

def test_adv12_1():
    number_of_paths = adv12_1(test_caves_small)
    assert number_of_paths == len(test_paths_small)

def test_adv12_2():
    number_of_paths = adv12_2(test_caves_small)
    assert number_of_paths == 36