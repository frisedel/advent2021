from day15.adv15 import Node, adv15_1, adv15_2, construct_node, enlarge_map
from test_input.test_data_day15 import small_map, large_map

def test_horistic():
    pass

def test_best_node():
    pass

def test_reconstruct_path():
    pass

def test_a_star():
    pass

def test_construct_node():
    node: Node = construct_node(0, 0, small_map)
    assert node.nodeID == '0:0'
    assert node.risk_value == 1
    assert node.x == 0
    assert node.y == 0
    assert len(node.neighbours) == 0

def test_update_node_neighbours():
    pass

def test_point_exist():
    pass

def test_create_map():
    pass

def test_enlarge_map():
    large = enlarge_map(small_map, 5)
    assert large == large_map

def test_adv15_1():
    total_risk = adv15_1(small_map)
    assert total_risk == 40

def test_adv15_2():
    total_risk = adv15_2(small_map)
    assert total_risk == 315
