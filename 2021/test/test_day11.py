from day11.adv11 import adv11_1, adv11_2, create_grid, grid_syncronized, observe_flashes

test_grid = [
    [5, 4, 8 ,3 ,1 ,4 ,3 ,2 ,2 ,3],
    [2, 7, 4 ,5 ,8 ,5 ,4 ,7 ,1 ,1],
    [5, 2, 6 ,4 ,5 ,5 ,6 ,1 ,7 ,3],
    [6, 1, 4 ,1 ,3 ,3 ,6 ,1 ,4 ,6],
    [6, 3, 5 ,7 ,3 ,8 ,5 ,4 ,7 ,8],
    [4, 1, 6 ,7 ,5 ,2 ,4 ,6 ,4 ,5],
    [2, 1, 7 ,6 ,8 ,4 ,1 ,7 ,2 ,1],
    [6, 8, 8 ,2 ,8 ,8 ,1 ,1 ,3 ,4],
    [4, 8, 4 ,6 ,8 ,4 ,8 ,5 ,5 ,4],
    [5, 2, 8 ,3 ,7 ,5 ,1 ,5 ,2 ,6]
]

test_grid_small = [
    [1, 2],
    [3, 4]
]

test_oct_small = [
        [{"x": 0, "y": 0, "value": 1, "last flash": 0, "flash num": 0}, {"x": 0, "y": 1, "value": 2, "last flash": 0, "flash num": 0}],
        [{"x": 1, "y": 0, "value": 3, "last flash": 0, "flash num": 0}, {"x": 1, "y": 1, "value": 4, "last flash": 0, "flash num": 0}]
    ]

test_grid_sync = [
        [{"x": 0, "y": 0, "value": 0, "last flash": 4, "flash num": 0}, {"x": 0, "y": 1, "value": 0, "last flash": 4, "flash num": 0}],
        [{"x": 1, "y": 0, "value": 0, "last flash": 4, "flash num": 0}, {"x": 1, "y": 1, "value": 0, "last flash": 4, "flash num": 0}]
    ]

def test_make_grid():
    small_oct_grid = create_grid(test_grid_small)
    assert small_oct_grid == test_oct_small

def test_observe_flashes():
    local = test_oct_small[:]
    observe_flashes(local, 1)
    assert local == [
        [{"x": 0, "y": 0, "value": 2, "last flash": 0, "flash num": 0}, {"x": 0, "y": 1, "value": 3, "last flash": 0, "flash num": 0}],
        [{"x": 1, "y": 0, "value": 4, "last flash": 0, "flash num": 0}, {"x": 1, "y": 1, "value": 5, "last flash": 0, "flash num": 0}]
    ]

def test_grid_syncronized():
    grid_not_synced = grid_syncronized(test_oct_small, 4)
    assert grid_not_synced == False
    grid_is_synced = grid_syncronized(test_grid_sync, 4)
    assert grid_is_synced == True

def test_adv11_1():
    flashes = adv11_1(test_grid)
    assert flashes == 1656

def test_adv11_2():
    iterations = adv11_2(test_grid)
    assert iterations == 195