from day13 import *

example_file = "test_day13input.txt"
example_list = load_file(example_file)
expected_list = []

def test_file_load():
    assert len(example_list[0]) == 18
    assert len(example_list[1]) == 2

def test_folding():
    assert fold_points(example_list[0], example_list[1][0]) == [[0, 3], [0, 13], [0, 14], [1, 10], [2, 14], [3, 0], [3, 4], [4, 1], [4, 4], [4, 11], [4, 12], [5, 0], [5, 10], [6, 0], [6, 4], [6, 10], [6, 12]]

fold0 = fold_points(example_list[0], example_list[1][0])
fold1 = fold_points(fold0, example_list[1][1])
print_point(example_list[0])
print_point(fold0)
print_point(fold1)
