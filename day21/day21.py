class Die(object):
    def __init__(self, rolls=0, side=0):
        self.rolls = 0
        self.side = 0

    def roll(self):
        self.rolls += 1
        if self.side == 100:
            self.side = 0
        self.side += 1
        #print("self.side:",self.side)
        return self.side

    def totalrolls(self):
        return self.rolls

class Player(object):
    def __init__(self, position, score=0):
        self.position = position
        self.score = score

    def move(self, dicetotal):
        self.position = self.position + (dicetotal % 10)
        if self.position > 10:
            self.position = self.position - 10
        self.score = self.score + self.position
        #print("new position:", self.position)
        return self.position

    def scorecheck(self):
        return self.score

    def position(self):
        return self.position

def play_game(start1, start2):
    player1 = Player(start1)
    player2 = Player(start2)
    die = Die()
    winner = False
    while not winner:
        roll1 = die.roll()
        roll2 = die.roll()
        roll3 = die.roll()
        dicetotal1 = roll1 + roll2 + roll3
        player1.move(dicetotal1)
        #print("player1 rolls",roll1,roll2,roll3,dicetotal1,"to space", player1.position, "for total score of", player1.scorecheck())
        if player1.scorecheck() >= 1000:
            print("winner player1")
            loserscore = player2.scorecheck()
            break
        roll1 = die.roll()
        roll2 = die.roll()
        roll3 = die.roll()
        dicetotal2 = roll1 + roll2 + roll3
        player2.move(dicetotal2)
        #print("player2 rolls",roll1,roll2,roll3,dicetotal2,"to space", player2.position, "for total score of", player2.scorecheck())
        if player2.scorecheck() >= 1000:
            loserscore = player1.scorecheck()
            print("winner player2")
            break
    print("totalrolls",die.totalrolls())
    print("loserscore",loserscore)
    solution = die.totalrolls() * loserscore
    return solution

testsolve = play_game(4, 8)
print("testsolve",testsolve)
part1 = play_game(8, 9)
print("part1:", part1)
