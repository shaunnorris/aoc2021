from day6 import *

example_file="test_day6input.txt"

def test_loadfile():
    example_day0_list = load_file(example_file)
    assert example_day0_list ==  [3, 4, 3, 1, 2]

def test_simulate_days():
    example_day0_list = load_file(example_file)
    assert simulate_day(example_day0_list, 18) == 26
    assert simulate_day(example_day0_list, 80) == 5934
    assert map_day(example_day0_list, 1) == 5
    assert map_day(example_day0_list, 2) == 6
    assert map_day(example_day0_list, 80) == 5934
