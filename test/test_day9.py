from day9.adv9 import adv9_1, adv9_2, as_global_dict, as_local_dict, calc_basin, calc_risks, find_global_lows, find_local_lows, in_any_basin, point_exist, points_to_add

test_map = [
    [2, 1, 9, 9, 9, 4, 3, 2, 1 ,0],
    [3, 9, 8, 7, 8, 9, 4, 9, 2, 1],
    [9, 8, 5, 6, 7, 8, 9, 8, 9, 2],
    [8, 7, 6, 7, 8, 9, 6, 7, 8 ,9],
    [9, 8, 9, 9, 9, 6, 5, 6, 7 ,8]
]
local_lat_zero = [{"long": 1, "value": 1}, {"long": 9, "value": 0}]
global_lows = [{'lat': 0, 'long': 1, 'value': 1}, {'lat': 0, 'long': 9, 'value': 0}, {'lat': 2, 'long': 2, 'value': 5}, {'lat': 4, 'long': 6, 'value': 5}]

ld = {"long": 2, "value": 9}

def test_local_dict():
    local_dict = as_local_dict(2, 9)
    assert local_dict == {"long": 2, "value": 9}

def test_global_dict():
    global_dict = as_global_dict(0, ld)
    assert global_dict == {"lat": 0, "long": 2, "value": 9}

def test_find_local_lows():
    local_lows = find_local_lows(test_map[0])
    assert local_lows == local_lat_zero

def test_find_global_lows():
    g_lows = find_global_lows(test_map)
    assert g_lows == global_lows

def test_calc_risk():
    def tk(d):
        if "risk value" in d:
            return True
        return False
    gl = global_lows[:]
    assert tk(gl[0]) == False
    calc_risks(gl)
    assert tk(gl[0]) == True and gl[0]["risk value"] == gl[0]["value"]+1

def test_adv9_1():
    risk = adv9_1(test_map)
    assert risk == 15


def test_in_basin():
    not_in_bas = in_any_basin(global_lows[0], [])
    assert not_in_bas == False
    in_bas = in_any_basin(global_lows[0], [global_lows])
    assert in_bas == True

def test_point_exist():
    p1 = point_exist((3,11), test_map)
    assert p1 == False
    p2 = point_exist((3, 9), test_map)
    assert p2 == True

def test_points_to_add():
    p1 = points_to_add(global_lows[0], test_map, [], [])
    assert p1 == [{'lat': 0, 'long': 0, 'value': 2, "can grow": True}]
    gl_extended = global_lows[:]
    gl_extended.append({'lat': 0, 'long': 0, 'value': 2, "can grow": False})
    p2 = points_to_add(global_lows[0], test_map, [], gl_extended)
    assert p2 == []

def test_calc_basin():
    gl = global_lows[:]
    gl[0]["can grow"] = True
    basin = calc_basin([gl[0]], test_map)
    assert basin == [{'lat': 0, 'long': 1, 'value': 1, 'risk value': 2, 'can grow': False}, {'lat': 0, 'long': 0, 'value': 2, 'can grow': False}, {'lat': 1, 'long': 0, 'value': 3, 'can grow': False}]
    assert len(basin) == 3

def test_adv9_2():
    value = adv9_2(test_map)
    assert value == 1134