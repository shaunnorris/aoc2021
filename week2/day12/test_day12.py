from day12 import *

example_file = "test_day12input.txt"
example_file2 = "test2_day12input.txt"
example_list = load_file(example_file)
example_list2 = load_file(example_file2)

expected_list = ['start-A', 'start-b', 'A-c', 'A-b', 'b-d', 'A-end', 'b-end']

def test_file_load():
    assert example_list == expected_list

def test_build_graph():
    assert build_graph(expected_list) ==  {'start': ['A', 'b'], 'A': ['start', 'c', 'b', 'end'], 'b': ['start', 'A', 'd', 'end'], 'c': ['A'], 'd': ['b'], 'end': ['A', 'b']}

def test_contains_repeated_lower():
    assert no_repeated_lower(['xxx'],['A','b','X','b'],) == False
    assert no_repeated_lower(['yyy'],['A','bx','X','bu']) == True

def test_find_all_paths():
    example_graph = build_graph(example_list)
    example_graph2 = build_graph(example_list2)

    assert len(find_all_paths(example_graph,'start','end')) == 10
    assert len(find_all_paths(example_graph2,'start','end')) == 19
    assert len(find_all_paths_pt2(example_graph,'start','end')) == 36
    assert len(find_all_paths_pt2(example_graph2,'start','end')) == 103
