#!/usr/bin/env python3

from typing import Dict, List

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


def find_basin(low: Dict[str, int]):
    pass


def adv9_2(smoke_map: List[List[int]]) -> int:
    global_lows = find_global_lows(smoke_map)
    basins = []
    for point in global_lows:
        find_basin(point)
    pass


def main():
    input_data = []
    with open("smoke_map.txt") as f:
        input_data = f.readlines()
    f.close

    smoke_map: List[List[int]] = []
    for line in input_data:
        smoke_map.append([int(i) for i in list(line.strip())])

    print("part 1 - :", adv9_1(smoke_map))
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