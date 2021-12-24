from day18 import *

example_file = "test_day18input.txt"
example_list = load_file(example_file)

expected_list = []

def test_file_load():
    assert example_list == expected_list

def test_find_explode():
#assert find_explode([[[[[9,8],1],2],3],4]) == [9,8]
#    assert find_explode([7,[6,[5,[4,[3,2]]]]]) == [3,2]
#    assert find_explode([[6,[5,[4,[3,2]]]],1]) == [3,2]
#    assert find_explode([[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]) == [7,3]
    assert find_explode([[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]) == [3,2]
