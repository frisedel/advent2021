#!/usr/bin/env python3

from day8.adv8 import adv8_1, adv8_2, all_in_signal, count_numbers, decode_signal, find_numbers, get_line_value, sort_strings, split_data

segment_text = [
    "be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe",
    "edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc",
    "fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg",
    "fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb",
    "aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea",
    "fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb",
    "dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe",
    "bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef",
    "egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb",
    "gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce"
]

one_segment_data = "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"
one_segment_in = ['acedgfb', 'cdfbe', 'gcdfa', 'fbcad', 'dab', 'cefabd', 'cdfgeb', 'eafb', 'cagedb', 'ab']
one_segment_out = ['cdfeb', 'fcadb', 'cdfeb', 'cdbaf']

one_segment_in_sorted = ['abcdefg', 'bcdef', 'acdfg', 'abcdf', 'abd', 'abcdef', 'bcdefg', 'abef', 'abcdeg', 'ab']
one_segment_out_sorted = ['bcdef', 'abcdf', 'bcdef', 'abcdf']
one_segment_mapped = {8: 'abcdefg', 7: 'abd', 4: 'abef', 1: 'ab', 3: 'abcdf', 9: 'abcdef', 0: 'abcdeg', 5: 'bcdef', 6: 'bcdefg', 2: 'acdfg'}

amount_numbers = {1: 8, 4: 6, 7: 5, 8: 7}

def test_find_numbers():
    numbers = find_numbers(segment_text)
    assert numbers == amount_numbers

def test_count_numbers():
    amount = count_numbers(amount_numbers)
    assert amount == 26

def test_adv8_1():
    amount = adv8_1(segment_text)
    assert amount == 26

def test_adv8_2():
    amount = adv8_2(segment_text)
    assert amount == 61229

def test_split():
    sig, val = split_data(one_segment_data)
    assert sig == one_segment_in
    assert val == one_segment_out

def test_sort_strings():
    sorted_strings = sort_strings(one_segment_in)
    assert sorted_strings == one_segment_in_sorted

def test_all_in():
    assert all_in_signal("ab", "abcdefg") == True
    assert all_in_signal("acdfg", "bcdef") == False

def test_decode_signal():
    sig_map = decode_signal(one_segment_in_sorted)
    assert sig_map == one_segment_mapped

def test_line_val():
    value = get_line_value(one_segment_in_sorted, one_segment_out_sorted)
    assert value == 5353