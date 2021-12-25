from day25 import *

example_file = "test_day25input.txt"
example_list = load_file(example_file)

expected_list = []

def test_file_load():
    assert len(example_list) == 9
    assert len(example_list[0]) == 10

def test_empty():
    assert is_empty(example_list, 0, 0) == (True, 1, 0) 
    assert is_empty(example_list, 0, 9) == (False, 0, 9)
    assert is_empty(example_list, 8, 9) == (True, 8, 0) 
    assert is_empty(example_list, 8, 4) == (False, 8, 4)

def test_move_herd():
    #assert len(move_herd(example_list)) == 9
    #assert len(move_herd(example_list[0])) == 10
    step1 = move_herd(example_list)
    assert step1[0] == '....>.>v.>'
    assert step1[8] == '>.v.v..v.v'
    step2 = move_herd(step1)
   
def test_find_no_moves():
    assert find_no_moves(example_list) == 58