from day20 import *

example_file = "test_day20input.txt"
example_list = load_file(example_file)
example_algo = example_list['algo']

expected_list = []

def test_file_load():
    assert len(example_list['algo']) == 512
    assert len(example_list['pic']) == 13
    assert len(example_list['pic'][0]) == 13

def test_get_index():
    assert get_index(example_list['pic'],1,1) == 0
    assert get_index(example_list['pic'],4,4) == 18
    assert get_index(example_list['pic'],6,6) == 34

def test_enhance_pic():
    pic2, pic2count = enhance(example_list)
    assert pic2count == 24
    example2 = {}
    example2['algo'] = example_algo
    example2['pic'] = pic2
    pic3, pic3count = enhance(example2)
    assert pic3count == 99
