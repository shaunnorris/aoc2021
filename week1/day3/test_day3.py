from day3 import *


example_input_list = ["00100",
                      "11110",
                      "10110",
                      "10111",
                      "10101",
                      "01111",
                      "00111",
                      "11100",
                      "10000",
                      "11001",
                      "00010",
                      "01010",
                      ]


def test_find_sub_common_list():
    assert find_most_common(example_input_list, 0) == True
    assert find_most_common(example_input_list, 1) == False
    assert find_most_common(example_input_list, 2) == True
    assert find_most_common(example_input_list, 3) == True
    assert find_most_common(example_input_list, 4) == False
    assert find_sub_common_list(example_input_list, 1) == ['1','0','1','1','0']
    assert find_sub_common_list(example_input_list, 0) == ['0','1','0','0','1']

def test_find_power():
    assert find_sub_power(example_input_list) == 198



def test_find_lifesupport():
    assert find_sub_ox_rating(example_input_list) == 23
    assert find_sub_co2_rating(example_input_list) == 10
    assert find_sub_lifesupport(example_input_list) == 230
