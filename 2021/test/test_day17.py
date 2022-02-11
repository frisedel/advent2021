from day17.adv17 import adv17_1, adv17_2, calculate_target_area, can_hit_target_area, get_vx_min

test_taget_area_data = 'target area: x=20..30, y=-10..-5'
test_target_area = {'x_min': 20, 'x_max': 30, 'y_min': -10, 'y_max': -5}

def test_calculate_target_area():
    ta = calculate_target_area(test_taget_area_data)
    assert ta == test_target_area

def test_get_vx_min():
    vx = get_vx_min(test_target_area["x_min"])
    assert vx == 6

def test_can_hit_target_area():
    can_hit = can_hit_target_area(6, 3, test_target_area)
    assert can_hit == True
    cant_hit = can_hit_target_area(5, 3, test_target_area)
    assert cant_hit == False

def test_adv17_1():
    max_y = adv17_1(test_target_area)
    assert max_y == 45

def test_adv17_2():
    number_of_hits = adv17_2(test_target_area)
    assert number_of_hits == 112