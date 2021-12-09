from day10 import *

example_file = "test_dayXYZinput.txt"
example_list = load_file(example_file)

expected_list = []

def test_file_load():
    assert example_list == expected_list
