from day15 import *

example_file = "test_day15input.txt"
example_list = load_file(example_file)

def test_file_load():
    assert example_list == len(example_list) == 10
