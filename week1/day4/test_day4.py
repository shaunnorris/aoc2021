from day4 import *


def test_load_example_game():
    example_game = create_game_from_file("test_day4input.txt")
    assert '17' in example_game['input']
    assert example_game['card2'][4] == ['2','0','12','3','7']


example_scorecard1 = [[14, 21, 17, 24, 4],
                      [10, 16, 15, 9, 19],
                      [18, 8, 23, 26, 20],
                      [22, 11, 13, 6, 5],
                      [2, 0, 12, 3, 0]]

example_scorecard2 = [[0, 0, 0, 0, 0],
                      [10, 16, 15, 9, 19],
                      [18, 8, 23, 26, 20],
                      [22, 11, 13, 6, 5],
                      [2, 0, 12, 3, 0]]

example_scorecard3 = [[1, 12, 0, 0, 0],
                      [10, 16, 15, 0, 19],
                      [18, 8, 23, 0, 20],
                      [22, 11, 13, 0, 5],
                      [2, 0, 12, 0, 0]]

def test_play_example_game():
    example_game = create_game_from_file("test_day4input.txt")
    assert check_winner(example_scorecard1) == False
    assert check_winner(example_scorecard2) == True
    assert check_winner(example_scorecard3) == True
    assert play_card(example_game['card2'],example_game['input']) == 4512
    assert play_bingo(example_game) == 4512, 11
