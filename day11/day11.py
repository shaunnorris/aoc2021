def load_file(filename):
    with open(filename) as f:
        mylist = f.read().splitlines()
    return mylist


def find_adjacents(mylist, x, y):
    adjacents = []
    maxx = len(mylist) - 1
    maxy = len(mylist[0]) - 1
    if x > 0:
        startx = x -1
    else:
        startx = 0
    if x < maxx:
        endx = x + 1
    else:
        endx = maxx
    if y > 0:
        starty = y - 1
    else:
        starty = 0
    if y < maxy:
        endy = y +1
    else:
        endy = maxy

    for row in range(startx,endx+1):
        for col in range(starty,endy+1):
            if [x,y] != [row,col]:
                adjacents.append([row,col])

    return adjacents

def inc_or_flash(input):
    if input == 'F':
        return 'F'
    elif int(input) < 9:
        return str(int(input)+1)
    elif int(input) == 9:
        return 'F'

def run_step(mylist):
    results = {}
    newlist = []
    flashes = 0

    #step A: add one to every cell
    for row in range(len(mylist)):
        newrow = []
        for col in range(len(mylist[0])):
            current = (mylist[row][col])
            newrow.append(inc_or_flash(current))
        newlist.append(newrow)

    #step B: find all cells that have flashed initially
    flashqueue = []
    flashed = []
    for row in range(len(mylist)):
        for col in range(len(mylist[0])):
            if newlist[row][col] == 'F':
                flashqueue.append([row,col])
                flashed.append([row,col])

    #recursively work through the flash adjacents and calculate flashes
    while len(flashqueue) > 0:
        for point in flashqueue:
            newpoints = find_adjacents(newlist,point[0],point[1])
            for newpoint in newpoints:
                if newpoint not in flashed:
                    newvalue = inc_or_flash(newlist[newpoint[0]][newpoint[1]])
                    if newvalue == 'F':
                        flashed.append(newpoint)
                        flashqueue.append(newpoint)
                    newlist[newpoint[0]][newpoint[1]] = newvalue
            flashqueue.remove(point)

    #finally replace all F with 0
    finallist = []
    for entry in newlist:
        newentry = [item.replace('F', '0') for item in entry]
        finallist.append(newentry)

    return finallist, len(flashed)

def run_days(mylist, days):
    flashcount = 0
    runlist = mylist
    for x in range(days):
        results = run_step(runlist)
        flashcount += results[1]
        runlist = results[0]
    return flashcount

def run_until_all_flash(mylist):
    runcount = 0
    runlist = mylist
    while True:
        runcount += 1
        results = run_step(runlist)
        flashcount = results[1]
        runlist = results[0]
        if flashcount == 100:
            return runcount


input_file = "day11input.txt"
input_list = load_file(input_file)

part1 = run_days(input_list,100)
print(part1)
part2 = run_until_all_flash(input_list)
print(part2)
