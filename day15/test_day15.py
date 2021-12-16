from day15 import *

example_file = "simple_day15input.txt"
example_list = load_file(example_file)
print(example_list)

def test_file_load():
    assert len(example_list) == 3

def test_build_graph():
    assert type(build_graph(example_list)) is dict

def test_find_path():
    test_graph = build_graph(example_list)
    assert find_path(test_graph) == True
