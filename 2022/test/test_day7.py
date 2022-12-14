from collections import defaultdict
from pathlib import PosixPath
from day7.adv_7 import adv7_1, adv7_2, make_file_system
from test_input.test_data_day7 import test_file_data

test_filesystem = defaultdict(int, {PosixPath('/'): 48381165, PosixPath('/a'): 94853, PosixPath('/a/e'): 584, PosixPath('/d'): 24933642})

def test_make_filesystem():
    filesystem = make_file_system(test_file_data)
    assert filesystem == test_filesystem

def test_adv7_1():
    filesystem = make_file_system(test_file_data)
    size = adv7_1(filesystem)
    assert size == 95437

def test_adv7_2():
    filesystem = make_file_system(test_file_data)
    size = adv7_2(filesystem)
    assert size == 24933642