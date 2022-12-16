import numpy as np

from day8.adv_8 import adv8_1, map_forest
from test_input.test_data_day8 import test_reforestation_data

test_forest: np.ndarray = np.array([[3, 0, 3, 7, 3], [2, 5, 5, 1, 2], [6, 5, 3, 3, 2], [3, 3, 5, 4, 9], [3, 5, 3, 9, 0]])

def test_map_forest():
    forest = map_forest(test_reforestation_data)
    assert forest.all() == test_forest.all()

def test_adv8_1():
    count = adv8_1(test_forest)
    print(count)
    assert count == 21