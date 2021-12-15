"""Day 9."""
from day9 import *


example_file = "test_day9input.txt"
example_list = load_file(example_file)

expected_list = ['2199943210',
                 '3987894921',
                 '9856789892',
                 '8767896789',
                 '9899965678']

def test_file_load():
    assert example_list == expected_list

def test_find_neighbours():
    assert find_neighbours(example_list, 0, 0) == [3, 1]
    assert find_neighbours(example_list, 0, 9) == [1, 1]
    assert find_neighbours(example_list, 0, 5) ==  [9, 9, 3]
    assert find_neighbours(example_list, 2, 2) ==  [8, 6, 8, 6]
    assert find_neighbours(example_list, 4, 9) ==   [9, 7]

def test_find_low_points():
    assert find_low_points(example_list) == [1,0,5,5]

def test_calculate_risk():
    lowpoints = find_low_points(example_list)
    assert calculate_risk(lowpoints) == 15

def test_find_basin_neighbours():
    assert find_basin_neighbours(example_list, 0, 1) == [[0,0]]
    assert find_basin_neighbours(example_list, 1, 2) == [[2, 2], [1, 3]]

def test_find_basin():
    assert find_basin(example_list, 2, 3) == 14
    assert find_basin(example_list, 4, 9) == 9
    assert find_basin(example_list, 0, 9) == 9
    assert find_basin(example_list, 0, 0) == 3

def test_find_3_largest_basins():
    assert find_3_largest_basins(example_list) == 1134
#def test_find_basin_size():
#    assert find_basin_size(example_list,1,2) == 14
