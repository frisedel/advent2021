from day14.adv14 import adv14_1, adv14_2, calculate_first_pairs, construct_polymer_str_extentions, count_elements, extend_polymer_string, get_element_comp, get_maxmin, get_polymer_dict_diff, process_polymer

test_template = 'NNCB'
test_polymer_1 = 'NCNBCHB'
test_polymer_4 = 'NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB'
test_polymer_4_comp = {'N': 11, 'B': 23, 'C': 10, 'H': 5}
test_polymer_pairs_4 = {'NB': 9, 'BB': 9, 'BN': 6, 'BC': 4, 'CC': 2, 'CN': 3, 'NC': 1, 'CB': 5, 'BH': 3, 'HC': 3, 'HH': 1, 'HN': 1, 'NH': 1}
test_first_pairs = {'NN': 1, 'NC': 1, 'CB': 1}
test_ext = [
    'CH -> B',
    'HH -> N',
    'CB -> H',
    'NH -> C',
    'HB -> C',
    'HC -> B',
    'HN -> C',
    'NN -> C',
    'BH -> H',
    'NC -> B',
    'NB -> B',
    'BN -> B',
    'BB -> N',
    'BC -> B',
    'CC -> N',
    'CN -> C'
]
test_extend_polymer_single = {'CH': 'B', 'HH': 'N', 'CB': 'H', 'NH': 'C', 'HB': 'C', 'HC': 'B', 'HN': 'C', 'NN': 'C', 'BH': 'H', 'NC': 'B', 'NB': 'B', 'BN': 'B', 'BB': 'N', 'BC': 'B', 'CC': 'N', 'CN': 'C'}
test_extend_polymer_double = {'CH': 'CB', 'HH': 'HN', 'CB': 'CH', 'NH': 'NC', 'HB': 'HC', 'HC': 'HB', 'HN': 'HC', 'NN': 'NC', 'BH': 'BH', 'NC': 'NB', 'NB': 'NB', 'BN': 'BB', 'BB': 'BN', 'BC': 'BB', 'CC': 'CN', 'CN': 'CC'}

def test_construct_polymer_extentions():
    extentions = construct_polymer_str_extentions(test_ext)
    print(extentions)
    assert extentions == test_extend_polymer_double

def test_extend_polymer():
    extended = extend_polymer_string(test_template, test_extend_polymer_double)
    print(extended)
    assert extended == test_polymer_1

def test_get_element_comp():
    elem_comp = get_element_comp(test_polymer_4)
    assert elem_comp == test_polymer_4_comp

def test_get_maxmin():
    max, min = get_maxmin(test_polymer_4_comp)
    assert max == 23
    assert min == 5

def test_adv14_1():
    element_value = adv14_1(test_template, test_extend_polymer_double)
    assert element_value == 1588

def test_calculate_first_pairs():
    first_pairs = calculate_first_pairs(test_template)
    assert first_pairs == {'NN': 1, 'NC': 1, 'CB': 1}

def test_get_polymer_dict_diff():
    diff = get_polymer_dict_diff(test_template, test_extend_polymer_single, 10)
    assert diff == 1588

def test_process_polymer():
    polymer = process_polymer(test_first_pairs, test_extend_polymer_single, 4)
    assert polymer == test_polymer_pairs_4

def test_count_elements():
    count = count_elements(test_polymer_pairs_4, test_template[-1])
    assert count == test_polymer_4_comp

def test_adv14_2():
    element_value = adv14_2(test_template, test_extend_polymer_single)
    assert element_value == 2188189693529