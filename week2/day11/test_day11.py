from day11 import *

example_file = "test_day11input.txt"
example_list = load_file(example_file)

expected_list = ['11111','19991','19191','19991','11111']

def test_file_load():
    assert example_list == expected_list

def test_find_adjacemnts():
    assert find_adjacents(example_list,0,0) == [[0, 1], [1, 0], [1, 1]]
    assert find_adjacents(example_list,4,4) ==  [[3, 3], [3, 4], [4, 3]]
    assert find_adjacents(example_list,0,4) == [[0, 3], [1, 3], [1, 4]]
    assert find_adjacents(example_list,4,0) ==  [[3, 0], [3, 1], [4, 1]]
    assert find_adjacents(example_list,0,2) == [[0, 1], [0, 3], [1, 1], [1, 2], [1, 3]]
    assert find_adjacents(example_list,2,0) ==  [[1, 0], [1, 1], [2, 1], [3, 0], [3, 1]]
    assert find_adjacents(example_list,2,4) ==  [[1, 3], [1, 4], [2, 3], [3, 3], [3, 4]]
    assert find_adjacents(example_list,4,2) ==  [[3, 1], [3, 2], [3, 3], [4, 1], [4, 3]]
    assert find_adjacents(example_list,1,1) == [[0, 0], [0, 1], [0, 2], [1, 0], [1, 2], [2, 0], [2, 1], [2, 2]]
    assert find_adjacents(example_list,3,3) ==  [[2, 2], [2, 3], [2, 4], [3, 2], [3, 4], [4, 2], [4, 3], [4, 4]]



example_file2 = "test2_day11input.txt"
example_list2 = load_file(example_file2)

def test_run_n_days():
    assert run_days(example_list2,10) == 204

def test_run_until_all_flash():
    assert run_until_all_flash(example_list2) == 195
