from day17.adv17 import adv17_1, calculate_target_area

test_taget_area_data = 'target area: x=20..30, y=-10..-5'
test_target_area = {'x_min': 20, 'x_max': 30, 'y_min': -10, 'y_max': -5}

def test_calculate_target_area():
    ta = calculate_target_area(test_taget_area_data)
    assert ta == test_target_area

def test_adv17_1():
    ta = calculate_target_area(test_taget_area_data)
    max_y = adv17_1(ta)
    assert max_y == 45