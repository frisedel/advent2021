from day8.adv_8 import map_forest
from test_input.test_data_day8 import test_reforestation_data

test_forest = [[3, 0, 3, 7, 3], [2, 5, 5, 1, 2], [6, 5, 3, 3, 2], [3, 3, 5, 4, 9], [3, 5, 3, 9, 0]]

def test_map_forest():  #rewrite to np array
    forest = map_forest(test_reforestation_data)
    assert forest == test_forest