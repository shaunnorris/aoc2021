"""AOC2021 day1."""
from day1 import *


example_depth_list = [199,
                        200,
                        208,
                        210,
                        200,
                        207,
                        240,
                        269,
                        260,
                        263]


def test_example_list_simple():
    """test that we find consecutive increases in a list."""
    assert find_increases(example_depth_list) == 7

def test_example_list_3way():
    """Test the 3-number windows to see how many are larger."""
    assert find_3way_increases(example_depth_list) == 5
