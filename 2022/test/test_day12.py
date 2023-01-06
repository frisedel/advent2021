from day12.adv_12 import Node, adv12_1, adv12_2, create_map
from test_input.test_data_day12 import test_topology

test_start: Node = Node("0:0", 0, 0, "S")
test_stop: Node = Node("5:2", 5, 2, "E")
test_map_ids = [
    '0:0', '1:0', '2:0', '3:0', '4:0', '5:0', '6:0', '7:0',
    '0:1', '1:1', '2:1', '3:1', '4:1', '5:1', '6:1', '7:1',
    '0:2', '1:2', '2:2', '3:2', '4:2', '5:2', '6:2', '7:2',
    '0:3', '1:3', '2:3', '3:3', '4:3', '5:3', '6:3', '7:3',
    '0:4', '1:4', '2:4', '3:4', '4:4', '5:4', '6:4', '7:4'
]

def test_create_map():
    map, start, stop = create_map(test_topology)
    print(test_start.node_id, test_stop.node_id)
    assert start == test_start.node_id
    assert stop == test_stop.node_id
    for i, node in enumerate(map):
        assert node == test_map_ids[i]

def test_adv12_1():
    map, start, stop = create_map(test_topology)
    test_steps = adv12_1(map, start, stop)
    assert test_steps == 31

def test_adv12_2():
    map, start, stop = create_map(test_topology)
    test_min_steps = adv12_2(map, start, stop)
    assert test_min_steps == 29