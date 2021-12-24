from day21 import *

def test_dice_rolls():
    testdice = Die()
    assert testdice.roll() == 1
    testdice2 = Die()
    for n in range(100):
        result = testdice2.roll()
        assert result == n+1
    result = testdice2.roll()
    assert result == 1
    assert testdice2.totalrolls() == 101

def test_player_move():
    player1 = Player(4)
    player1.move(6)
    assert player1.scorecheck() == 10
    player1.move(24)
    assert player1.scorecheck() == 14
    player1.move(42)
    assert player1.scorecheck() == 20
    player1.move(60)
    assert player1.scorecheck() == 26
