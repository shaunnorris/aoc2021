from day22 import *

smalltest_file = "smalltest_day22input.txt"
smalltest_list = load_file(smalltest_file)

smalltest_expected =  ['on x=10..12,y=10..12,z=10..12', 'on x=11..13,y=11..13,z=11..13', 'off x=9..11,y=9..11,z=9..11', 'on x=10..10,y=10..10,z=10..10']

test_file = "test_day22input.txt"
test_list = load_file(test_file)

test_expected =  []

def test_file_load():
    assert smalltest_list == smalltest_expected

def test_read_instruction():
    assert read_instruction(smalltest_list[0]) == {'onoff': 'on', 'x': [10, 11, 12], 'y': [10, 11, 12], 'z': [10, 11, 12]}
    assert read_instruction(smalltest_list[1]) == {'onoff': 'on', 'x': [11, 12, 13], 'y': [11, 12, 13], 'z': [11, 12, 13]}
    assert read_instruction(smalltest_list[2]) == {'onoff': 'off', 'x': [9, 10, 11], 'y': [9, 10, 11], 'z': [9, 10, 11]}
    assert read_instruction(smalltest_list[3]) == {'onoff': 'on', 'x': [10], 'y': [10], 'z': [10]}
    #assert read_instruction(test_list[0]) == {'onoff': 'on', 'x': [-20, -19, -18, -17, -16, -15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26], 'y': [-36, -35, -34, -33, -32, -31, -30, -29, -28, -27, -26, -25, -24, -23, -22, -21, -20, -19, -18, -17, -16, -15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], 'z': [-47, -46, -45, -44, -43, -42, -41, -40, -39, -38, -37, -36, -35, -34, -33, -32, -31, -30, -29, -28, -27, -26, -25, -24, -23, -22, -21, -20, -19, -18, -17, -16, -15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7]}

def test_reduce_instructions():
    assert reduce_instructions(smalltest_list) == False

def test_initialise():
    assert initialise(smalltest_list) == 39
    #assert initialise(test_list) == False
