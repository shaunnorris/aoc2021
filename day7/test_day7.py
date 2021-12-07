from day7 import *

example_file = "test_day7input.txt"
example_list = load_file(example_file)

def test_loadfile():
    assert example_list ==  [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]

def test_find_best_position():
    assert find_best_position(example_list) == 37

def test_part2_best_position():
    assert find_best_part2_position(example_list) == 168
