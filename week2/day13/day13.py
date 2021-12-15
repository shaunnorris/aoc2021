def load_file(filename):
    pointlist = []
    foldlist = []
    with open(filename) as f:
        mylist = f.read().splitlines()
    for entry in mylist:
        if "," in entry:
            point = entry.split(',')
            point = list(map(int, point))
            pointlist.append(point)
        if "=" in entry:
            fold = entry.split(" ")[2]
            foldlist.append(fold.split('='))
    return [pointlist, foldlist]


def fold_points(pointlist, fold):
    axis = fold[0]
    foldline = int(fold[1])
    newlist = []
    if axis == 'x':
        for x, y in pointlist:
            if x > foldline:
                distance = x - foldline
                newx = foldline - distance
                if [newx, y] not in pointlist:
                    newlist.append([newx, y])
            else:
                newlist.append([x, y])
    elif axis == 'y':
        for x, y in pointlist:
            if y > foldline:
                distance = y - foldline
                newy = foldline - distance
                newlist.append([x, newy])
            else:
                newlist.append([x, y])
    return sorted(newlist)


def print_point(pointlist):
    maxx = 0
    maxy = 0
    for point in sorted(pointlist):
        if point[0] > maxx:
            maxx = point[0]
        if point[1] > maxy:
            maxy = point[1]
    for y in range(maxy+1):
        str = ""
        for x in range(maxx+1):
            if [x,y] in pointlist:
                str = str + "#"
            else:
                str = str + "."
        print(str)


def solve_puzzle(inputlist):
    prefold = inputlist[0]
    folds = inputlist[1]
    for fold in folds:
        newlist = fold_points(prefold,fold)
        prefold = newlist
    return newlist

puzzle_input = load_file("day13input.txt")
part1 = fold_points(puzzle_input[0], puzzle_input[1][0])
print(len(part1))
part2 = solve_puzzle(puzzle_input)
print_point(part2)
