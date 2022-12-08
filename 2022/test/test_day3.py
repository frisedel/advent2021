from day3.adv_3 import adv3_1, adv3_2, create_groups, find_badge, find_duplicates, search_rucksack, split_content
from test_input.test_data_day3 import test_content

test_part1, test_part2 = "vJrwpWtwJgWr", "hcsFMMfFFhFp"

test_rucksacks = [('vJrwpWtwJgWr', 'hcsFMMfFFhFp'), ('jqHRNqRjqzjGDLGL', 'rsFMfFZSrLrFZsSL'), ('PmmdzqPrV', 'vPwwTWBwg'), ('wMqvLMZHhHMvwLH', 'jbvcjnnSBnvTQFn'), ('ttgJtRGJ', 'QctTZtZT'), ('CrZsJsPPZsGz', 'wwsLwLmpwMD')]
test_duplicates = ['p', 'L', 'P', 'v', 't', 's']

test_groups = [['vJrwpWtwJgWrhcsFMMfFFhFp', 'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL', 'PmmdzqPrVvPwwTWBwg'], ['wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn', 'ttgJtRGJQctTZtZT', 'CrZsJsPPZsGzwwsLwLmpwMDw']]

def test_split_content():
    part1, part2 = split_content(test_content[0])
    assert part1 == test_part1
    assert part2 == test_part2

def test_find_duplicates():
    duplicates = find_duplicates(test_rucksacks)
    assert duplicates == test_duplicates

def test_search_rucksack():
    duplicate_items1 = search_rucksack(test_rucksacks[0])
    assert duplicate_items1 == ['p']
    duplicate_items2 = search_rucksack(test_rucksacks[1])
    assert duplicate_items2 == ['L']

def test_adv3_1():
    count = adv3_1(test_content)
    assert count == 157

def test_create_groups():
    groups = create_groups(test_content)
    assert groups == test_groups

def test_find_badge():
    badge = find_badge(test_groups[0])
    assert badge == 'r'

def test_adv3_2():
    priority_sum = adv3_2(test_content)
    assert priority_sum == 70