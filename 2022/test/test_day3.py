from day3.adv_3 import create_rucksacks, find_duplicates, split_content
from test_input.test_data_day3 import test_content

test_part11, test_part12 = "vJrwpWtwJgWr", "hcsFMMfFFhFp"
test_part21, test_part22 = "jqHRNqRjqzjGDLGL", "rsFMfFZSrLrFZsSL"

test_rucksacks = [('vJrwpWtwJgWr', 'hcsFMMfFFhFp'), ('jqHRNqRjqzjGDLGL', 'rsFMfFZSrLrFZsSL'), ('PmmdzqPrV', 'vPwwTWBwg'), ('wMqvLMZHhHMvwLH', 'jbvcjnnSBnvTQFn'), ('ttgJtRGJ', 'QctTZtZT'), ('CrZsJsPPZsGz', 'wwsLwLmpwMD')]

def test_split_content():
    part11, part12 = split_content(test_content[0])
    assert part11 == test_part11
    assert part12 == test_part12
    part21, part22 = split_content(test_content[1])
    assert part21 == test_part21
    assert part22 == test_part22

def test_find_duplicates():
    duplicates = find_duplicates(test_rucksacks)
    print(duplicates)
    assert duplicates == ['v', 'P', 'L', 's', 'p', 't']

def test_sum_priority():
    return

