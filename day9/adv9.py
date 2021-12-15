#!/usr/bin/env python3

from typing import Dict, List, Tuple

def as_local_dict(long: int, value: int) -> Dict[str, int]:
    return {"long": long, "value": value}


def as_global_dict(lat, local) -> Dict[str, int]:
    return {"lat": lat, "long": local["long"], "value": local["value"]}


def find_local_lows(latitude: List[int]) -> List[Dict[str, int]]:
    latitude_length = len(latitude)
    last_index = latitude_length-1
    local_lows: List[Dict[str, int]] = []
    if latitude[0] < latitude[1]:
        local_lows.append(as_local_dict(0, latitude[0]))
    for index in range(1, latitude_length-1):
        if latitude[index-1] > latitude[index] < latitude[index+1]:
            local_lows.append(as_local_dict(index, latitude[index]))
    if latitude[last_index] < latitude[last_index-1]:
        local_lows.append(as_local_dict(last_index, latitude[last_index]))
    return local_lows


def find_global_lows(smoke_map: List[List[int]]):
    global_lows: List[Dict[str, int]] = []
    last_lat = len(smoke_map)-1
    for lat_index in range(len(smoke_map)):
        local_lows = find_local_lows(smoke_map[lat_index])
        for local in local_lows:
            if lat_index == 0:
                if smoke_map[1][local["long"]] > local["value"]:
                    global_lows.append(as_global_dict(lat_index, local))
            elif lat_index == last_lat:
                if smoke_map[lat_index-1][local["long"]] > local["value"]:
                    global_lows.append(as_global_dict(lat_index, local))
            elif smoke_map[lat_index-1][local["long"]] > local["value"] and smoke_map[lat_index+1][local["long"]] > local["value"]:
                global_lows.append(as_global_dict(lat_index, local))
    return global_lows


def calc_risks(global_lows: List[Dict[str, int]]):
    for low in global_lows:
        risk = low["value"]+1
        low["risk value"]= risk


def adv9_1(smoke_map: List[List[int]]) -> int:
    global_lows = find_global_lows(smoke_map)
    calc_risks(global_lows)
    total_risk = 0
    for low_point in global_lows:
        total_risk += low_point["risk value"]
    return total_risk


def in_any_basin(point: Dict[str, int], basins: List[List[Dict[str, int]]]) -> bool:
    #loop over all basins and see if point inside it. need try/except for first go.
    for basin in basins:
        try:
            for basin_point in basin:
                if point["lat"] == basin_point["lat"] and point["long"] == basin_point["long"]:
                    return True
            return False
        except:
            return False


def point_exist(lat_long: Tuple[int, int], smoke_map: List[List[int]]) -> bool:
    max_lat = len(smoke_map)-1
    max_long = len(smoke_map[0])-1
    return 0 <= lat_long[0] <= max_lat and 0 <= lat_long[1] <= max_long


#def points_to_add - take point and mapp
def points_to_add(point: Dict[str, int], smoke_map: List[List[int]]):
    #   [.....]
    #   [--a--]
    #   [-cPd-]
    #   [--b--]
    #   [.....]

    a = (point["lat"]-1, point["long"])
    b = (point["lat"]+1, point["long"])
    c = (point["lat"], point["long"]-1)
    d = (point["lat"], point["long"]+1)

    points = []

    if point_exist(a, smoke_map) and smoke_map[a[0]][a[1]] != 9:
        points.append({"lat": a[0], "long": a[1], "value": smoke_map[a[0]][a[1]], "can grow": True})
    if point_exist(b, smoke_map) and smoke_map[b[0]][b[1]] != 9:
        points.append({"lat": b[0], "long": b[1], "value": smoke_map[b[0]][b[1]], "can grow": True})
    if point_exist(c, smoke_map) and smoke_map[c[0]][c[1]] != 9:
        points.append({"lat": c[0], "long": c[1], "value": smoke_map[c[0]][c[1]], "can grow": True})
    if point_exist(d, smoke_map) and smoke_map[d[0]][d[1]] != 9:
        points.append({"lat": d[0], "long": d[1], "value": smoke_map[d[0]][d[1]], "can grow": True})
    # 1 see if the points around exists
    # 2 see if points not 9
    # 3 add point to list to return and set 'can_grow' to false
    return points


def calc_basin(point: Dict[str, int], smoke_map: List[List[int]]):
    print("calc basin")
    start = {"lat": point["lat"], "long": point["long"], "value": point["value"], "can grow": True}
    basin = [start]

    growing = True
    while growing:
        growing = False
        for point in basin:
            print(point)
            new_points = []
            if point["can grow"] and not in_any_basin(point, [basin]):
                new_points = points_to_add(point, smoke_map)
                point["can grow"] = False
            if len(new_points) > 0:
                growing = True
            basin = basin + new_points
    return basin


def adv9_2(smoke_map: List[List[int]]) -> int:
    global_lows = find_global_lows(smoke_map)
    basins: List[List[Dict[str, int]]] = []
    for point in global_lows:
        if not in_any_basin(point, basins):
            basins.append(calc_basin(point, smoke_map))
    # find longest 3 basins, easy since it is lists
    # multiply lengths
    # return value
    return 0


def main():
    input_data = []
    with open("smoke_map.txt") as f:
        input_data = f.readlines()
    f.close

    smoke_map: List[List[int]] = []
    for line in input_data:
        smoke_map.append([int(i) for i in list(line.strip())])

    print("part 1 - Total risk value:", adv9_1(smoke_map))
    print("part 2 - :", adv9_2(smoke_map))

if __name__ == '__main__':
    main()

"""
    === for first part ===
    1. read input
    2. convert to list of int
    3 loop over rows. if local low, take index and check above and below
    4. add low points to list
    5. calculate risk for points
    6. sum the risks
    7. return value
"""