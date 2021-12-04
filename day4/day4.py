def create_game_from_file(filename):
    with open(filename) as f:
        lines = f.readlines()
    testlist = []
    bingogame = {}
    bingogame['card0'] = {}
    bingogame['card0'][0] = []
    cardindex = -1
    rowindex = 0
    for line in lines:
        line = line.lstrip()
        if "," in line:
            bingogame['input'] = line.strip().split(",")
        elif len(line) > 0:
            bingogame['card'+str(cardindex)][rowindex] = []
            bingogame['card'+str(cardindex)][rowindex] = line.strip().split()
            rowindex += 1
        else:
            cardindex += 1
            rowindex = 0
            bingogame['card'+str(cardindex)] = {}
    return bingogame


def play_bingo(game):
    input = game['input']
    game.pop('input')
    lowmoves = 99
    winningscore = 0
    for i, (card, row) in enumerate(game.items()):
        score, moves = play_card(row, input)
        if moves < lowmoves:
            lowmoves = moves
            winningscore = score
            print("card:"+card+"now winning score:"+str(winningscore))
            print(str(moves)+" moves")
    return winningscore

def play_bingo_badly(game):
    input = game['input']
    game.pop('input')
    highmoves = 0
    winningscore = 0
    for i, (card, row) in enumerate(game.items()):
        score, moves = play_card(row, input)
        if moves > highmoves:
            highmoves = moves
            winningscore = score
            print("card:"+card+"now losing score:"+str(winningscore))
            print(str(moves)+" moves")
    return winningscore

def play_card(card,input):
    scorelist = []
    for i, (key, value) in enumerate(card.items()):
        scorelist.append(list(map(int, value)))
    for playnum in input:
        for row in card:
            if playnum in card[row]:
                index = card[row].index(playnum)
                scorelist[row][index] = 0
                if check_winner(scorelist):
                    score = 0
                    for row in scorelist:
                        score += sum(row)
                    moves = input.index(playnum)
                    score = score * int(playnum)
                    return score, moves
    return False


def check_winner(scorecard):
    """check rows then transpose table to check columns."""
    for row in scorecard:
        if sum(row) == 0:
            return True
    for row in list(map(list, zip(*scorecard))):
        if sum(row) == 0:
            return True
    return False

part1_game = create_game_from_file("day4input.txt")
part1 = play_bingo(part1_game)
print(part1)
part2_game = create_game_from_file("day4input.txt")
part2 = play_bingo_badly(part2_game)
print(part2)
