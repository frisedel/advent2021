from test_input.test_data_day3 import test_content

test_part1, test_part2 = "vJrwpWtwJgWr", "hcsFMMfFFhFp"

def test_split_content(content:str):
    part1, part2 = split_content(test_content[0])
    assert part1 == test_part1
    assert part2 == test_part2

def test_sum_duplicates():
    return

