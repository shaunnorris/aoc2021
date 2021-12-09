from day5 import *

example_points =  load_lines_from_file("test_day5input.txt")
expanded_points_part1 = expand_points_part1(example_points)
expanded_points_part2 = expand_points_part2(example_points)

def test_example_data():
    assert len(example_points) == 10
    assert [0, 9, 5, 9] in example_points
    assert [3, 4, 1, 4] in example_points

def test_expand_points_part1():
    assert len(expanded_points_part1) == 26

def test_count_overlaps_part1():
    assert find_overlaps(expanded_points_part1) == 5


def test_part2():
    part2_points = load_lines_from_file("test_day5input.txt")
    expanded_points_part2 = expand_points_part2(part2_points)
    overlaps_part2 = find_overlaps(expanded_points_part2)
    assert overlaps_part2 == 12
