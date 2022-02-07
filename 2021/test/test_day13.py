from day13.adv13 import adv13_1, adv13_2, construct_coordinates, construct_paper, count_dots, extraxt_folds, fold_x, fold_y

test_coordinates_data = ['6,10', '0,14', '9,10', '0,3', '10,4', '4,11', '6,0', '6,12', '4,1', '0,13', '10,12', '3,4', '3,0', '8,4', '1,10', '2,14', '8,10', '9,0']
test_coordinates = [(6, 10), (0, 14), (9, 10), (0, 3), (10, 4), (4, 11), (6, 0), (6, 12), (4, 1), (0, 13), (10, 12), (3, 4), (3, 0), (8, 4), (1, 10), (2, 14), (8, 10), (9, 0)]
test_paper_start = [
    [0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
]

test_paper_after_first = [
    [1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 0, 1, 0, 2, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

test_final_paper = [
    [1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 2, 2, 1, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

test_final_text = '\n# # # # # \n# . . . # \n# . . . # \n# . . . # \n# # # # # \n. . . . . \n. . . . . \n'

test_fold_data = ['fold along y=7', 'fold along x=5']
test_folds = [('y', 7), ('x', 5)]

def test_construct_coordinates():
    coordinates = construct_coordinates(test_coordinates_data)
    assert coordinates == test_coordinates

def test_construct_paper():
    paper = construct_paper(test_coordinates)
    assert paper == test_paper_start

def test_extraxt_folds():
    folds = extraxt_folds(test_fold_data)
    assert folds == test_folds

def test_count_dots():
    number_dots = count_dots(test_final_paper)
    assert number_dots == 16

def test_fold_x():
    after = fold_x(test_paper_after_first, 5)
    assert after == test_final_paper

def test_fold_y():
    after = fold_y(test_paper_start, 7)
    print(after)
    assert after[0] == test_paper_after_first[0]

def test_adv13_1():
    num = adv13_1(test_paper_start, test_folds)
    assert num == 17

def test_adv13_2():
    square = adv13_2(test_paper_start, test_folds)
    assert square == test_final_text