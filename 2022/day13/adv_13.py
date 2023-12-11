#!/usr/bin/env python3

from copy import deepcopy
import json
from typing import Tuple


def compare_signals(left, right) -> bool:
    if not left and not right:
        return False, False

    if not left:
        return True, True

    if not right:
        return True, False

    if isinstance(left[0], int) and isinstance(right[0], int):
        if left[0] < right[0]:
            return True, True

        if right[0] < left[0]:
            return True, False
    
    elif isinstance(left[0], list) and isinstance(right[0], list):
        result, correct_order = compare_signals(deepcopy(left[0]), deepcopy(right[0]))
        if result:
            return result, correct_order

    elif isinstance(left[0], int) and isinstance(right[0], list):
        new_left = deepcopy(left)
        new_left[0] = [left[0]]
        return compare_signals(new_left, right)

    elif isinstance(left[0], list) and isinstance(right[0], int):
        new_right = deepcopy(right)
        new_right[0] = [right[0]]
        return compare_signals(left, new_right)
    else:
        assert False

    return compare_signals(deepcopy(left[1:]), deepcopy(right[1:]))


def adv13_1(distress_signal_data):
    indices = []

    for i in range(0, len(distress_signal_data), 2):
        _, correct_order = compare_signals(deepcopy(distress_signal_data[i]), deepcopy(distress_signal_data[i+1]))

        if correct_order:
            indices.append((i//2)+1)

    return sum(indices)


def adv13_2(distress_signal_data):
    distress_signal_data.extend([[[2]], [[6]]])

    return


def main():

    distress_signal_data = []
    with open("distress_signal_data.txt") as f:
        for line in f:
            try:
                distress_signal_data.append(json.loads(line))
            except:
                pass
    f.close()

    print("part 1 - Sum of orderd pair indecies:", adv13_1(distress_signal_data))
    print("part 2 - :", adv13_2(distress_signal_data))


if __name__ == '__main__':
    main()
