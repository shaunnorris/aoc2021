from day2 import *

sample_moves = ["forward 5",
              "down 5",
              "forward 8",
              "up 3",
              "down 8",
              "forward 2",
              ]

def test_example():
    assert pos_by_depth(sample_moves) == 150
    assert pos_by_depth_complex(sample_moves) == 900
