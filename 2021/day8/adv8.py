#!/usr/bin/env python3

from typing import Dict, List, Tuple

def find_numbers(data: List[str]):
    amount_numbers = {1:0, 4:0, 7:0, 8:0}
    others = 0
    for code in data:
        signal_values = code.split('|')[-1].strip().split()
        for value in signal_values:
            if len(value) == 2:
                amount_numbers[1] += 1
            elif len(value) == 4:
                amount_numbers[4] += 1
            elif len(value) == 3:
                amount_numbers[7] += 1
            elif len(value) == 7:
                amount_numbers[8] += 1
            else:
                others += 1
    return amount_numbers


def count_numbers(numbers: Dict[int, int]):
    appearances = 0
    for number in numbers:
        appearances += numbers[number]
    return appearances


def adv8_1(data: List[str]):
    amount_numbers = find_numbers(data)
    number_of_appearances = count_numbers(amount_numbers)
    return number_of_appearances


def split_data(segment_data: str) -> Tuple[List[str], List[str]]:
    data = segment_data.split('|')
    return data[0].strip().split(), data[1].strip().split()


def sort_strings(strings) -> List[str]:
    local: List[str] = []
    for string in strings:
        local.append("".join(sorted(string)))
    return local


def all_in_signal(small: str, large: str) -> bool:
    small_signal = list(small)
    large_signal = list(large)
    for part in small_signal:
        if part not in large_signal:
            return False
    return True

def decode_signals(signals: List[str]) -> Dict[int, str]:
    unknown_signals = signals[:]
    numbers_map: Dict[int, str] = {}
    for signal in signals:
        if len(signal) == 2:
            numbers_map[1] = signal
            unknown_signals.remove(signal)
        elif len(signal) == 4:
            numbers_map[4] = signal
            unknown_signals.remove(signal)
        elif len(signal) == 3:
            numbers_map[7] = signal
            unknown_signals.remove(signal)
        elif len(signal) == 7:
            numbers_map[8] = signal
            unknown_signals.remove(signal)

    while len(unknown_signals) > 0:
        for signal in unknown_signals:  # 235
            if len(signal) == 5:
                if all_in_signal(numbers_map[7], signal):   #3
                    numbers_map[3] = signal
                    unknown_signals.remove(signal)
                elif 9 in numbers_map.keys() and all_in_signal(signal, numbers_map[9]):    #5
                    numbers_map[5] = signal
                    unknown_signals.remove(signal)
                elif 3 in numbers_map.keys() and 5 in numbers_map.keys(): #2
                    numbers_map[2] = signal
                    unknown_signals.remove(signal)

            elif len(signal) == 6:    # 069
                if all_in_signal(numbers_map[4], signal):   #9
                    numbers_map[9] = signal
                    unknown_signals.remove(signal)
                elif 9 in numbers_map.keys() and all_in_signal(numbers_map[7], signal): #0
                    numbers_map[0] = signal
                    unknown_signals.remove(signal)
                elif 9 in numbers_map.keys() and 0 in numbers_map.keys():   #6
                    numbers_map[6] = signal
                    unknown_signals.remove(signal)

    return numbers_map


def get_line_value(signals: List[str], values: List[str]) -> int:
    signal_map = decode_signals(signals)

    line_value: List[int] = []
    for signal_value in values:
        for key, value in signal_map.items():
            if signal_value == value:
                line_value.append(key)

    return int(''.join(map(str,line_value)))


def adv8_2(data: List[str]) -> int:
    total = 0
    for line in data:
        signals, values = split_data(line)
        sorted_signals = sort_strings(signals)
        sorted_values = sort_strings(values)
        total += get_line_value(sorted_signals, sorted_values)
    return total


def main():
    input_data = []
    with open("seven_segment.txt") as f:
        input_data = f.readlines()
    f.close

    data: List[str] = []
    for code in input_data:
        data.append(code.strip())

    print("part 1 - number of apperances:", adv8_1(data))
    print("part 2 - sum of all values:", adv8_2(data))

if __name__ == '__main__':
    main()