from day14.adv14 import adv14_1, adv14_2, construct_polymer_extentions, extend_polymer, get_element_comp, get_maxmin

test_template = 'NNCB'
test_polymer_1 = 'NCNBCHB'
test_polymer_4 = 'NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB'
test_polymer_4_comp = {'N': 11, 'B': 23, 'C': 10, 'H': 5}

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

test_polymer_map = {'CH': 'CB', 'HH': 'HN', 'CB': 'CH', 'NH': 'NC', 'HB': 'HC', 'HC': 'HB', 'HN': 'HC', 'NN': 'NC', 'BH': 'BH', 'NC': 'NB', 'NB': 'NB', 'BN': 'BB', 'BB': 'BN', 'BC': 'BB', 'CC': 'CN', 'CN': 'CC'}

def test_construct_polymer_extentions():
    extentions = construct_polymer_extentions(test_ext)
    print(extentions)
    assert extentions == test_polymer_map

def test_extend_polymer():
    extended = extend_polymer(test_template, test_polymer_map)
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
    element_value = adv14_1(test_template, test_polymer_map)
    assert element_value == 1588

def test_adv14_2():
    element_value = adv14_2(test_template, test_polymer_map)
    assert element_value == 2188189693529