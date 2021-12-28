from copy import deepcopy
from day12.adv12 import adv12_1, navigate_caves, trim_graph

test_caves_small = {'start': ['A', 'b'], 'A': ['start', 'b', 'c', 'end'], 'b': ['start', 'A', 'd', 'end'], 'c': ['A'], 'd': ['b']}
test_caves_small_trimmed = {'start': ['A', 'b'], 'A': ['start', 'b', 'c', 'end'], 'b': ['start', 'A', 'end'], 'c': ['A']}

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

def test_trim_graph():
    local = deepcopy(test_caves_small)
    trim_graph(local)
    assert local == test_caves_small_trimmed

def test_navigate_caves():
    paths = []
    navigate_caves(test_caves_small_trimmed, paths, [], "start")
    assert paths == test_paths_small

def test_adv12_1():
    number_of_paths = adv12_1(test_caves_small_trimmed)
    assert number_of_paths == len(test_paths_small)

