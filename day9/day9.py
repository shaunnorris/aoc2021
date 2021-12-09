def load_file(filename):
    with open(filename) as f:
        mylist = f.read().splitlines()
    return mylist


def find_neighbours(maplist, x, y):
    adjacents = []
    maxx = len(maplist) - 1
    maxy = len(maplist[0]) - 1
    if x > 0:
        adjacents.append(maplist[x-1][y])
    if x < maxx:
        adjacents.append(maplist[x+1][y])
    if y > 0:
        adjacents.append(maplist[x][y-1])
    if y < maxy:
        adjacents.append(maplist[x][y+1])
    return list(map(int, adjacents))


def find_low_points(maplist):
    lowpoints = []
    for x in range(len(maplist)):
        for y in range(len(maplist[0])):
            adjacents = find_neighbours(maplist, x, y)
            if int(maplist[x][y]) < min(adjacents):
                lowpoints.append(int(maplist[x][y]))
    return lowpoints

def find_low_coords(maplist):
    lowpoints = []
    for x in range(len(maplist)):
        for y in range(len(maplist[0])):
            adjacents = find_neighbours(maplist, x, y)
            if int(maplist[x][y]) < min(adjacents):
                lowpoints.append([x, y])
    return lowpoints

def calculate_risk(lowpoints):
    risk_list = [x+1 for x in lowpoints]
    return sum(risk_list)

def find_basin_neighbours(maplist, x, y):
    adjacents = []
    maxx = len(maplist) - 1
    maxy = len(maplist[0]) - 1
    filtered = []
    if x > 0:
        adjacents.append([x-1,y])
    if x < maxx:
        adjacents.append([x+1,y])
    if y > 0:
        adjacents.append([x,y-1])
    if y < maxy:
        adjacents.append([x,y+1])
    for point in adjacents:
        if int(maplist[point[0]][point[1]]) != 9:
            filtered.append(point)
    return filtered

def find_basin(maplist, x , y):
    startpoint = [x , y]
    basin = []
    workqueue = []
    workqueue.append(startpoint)
    basin.append(startpoint)
    while len(workqueue) > 0:
        for point in workqueue:
            newpoints = find_basin_neighbours(maplist,point[0],point[1])
            for newpoint in newpoints:
                if newpoint not in basin:
                    workqueue.append(newpoint)
                    basin.append(newpoint)
            workqueue.remove(point)
    return len(basin)

def find_3_largest_basins(maplist):
    basinlist = []
    lowpoints = find_low_coords(maplist)
    for lowpoint in lowpoints:
        basinlist.append(find_basin(maplist,lowpoint[0], lowpoint[1]))
    basinlist.sort()
    top3list = basinlist[-3:]
    total = 1
    for element in top3list:
        total = total * element
    return total

file = "day9input.txt"
part1_list = load_file(file)
part1 = calculate_risk(find_low_points(part1_list))
print(part1)
part2 = find_3_largest_basins(part1_list)
print(part2)
