import re
from collections import Counter

def load_lines_from_file(filename):
    """Part1 ignore diagonals."""
    points_list = []
    with open(filename) as f:
        lines = f.readlines()
        for line in lines:
            linelist = re.split(r"->", line)
            x_start = int(linelist[0].split(',')[0])
            y_start = int(linelist[0].split(',')[1])
            x_end = int(linelist[1].split(',')[0])
            y_end = int(linelist[1].split(',')[1])
            points_list.append([x_start,y_start,x_end,y_end])
    return points_list


def expand_points_part1(points_list):
    """Part 1."""
    expanded_points = []
    for point_set in points_list:
        startx = point_set[0]
        starty = point_set[1]
        endx = point_set[2]
        endy = point_set[3]
        if startx == endx or starty == endy:
            if startx <= endx:
                x = list(range(startx, endx+1))
            elif startx > endx:
                x = list(range(startx,endx-1,-1))
            elif startx == endx:
                x = [startx]

            if starty <= endy:
                y = list(range(starty, endy+1))
            elif starty > endy:
                y = list(range(starty,endy-1,-1))
            elif starty == endy:
                y = [starty]

            if len(y) == 1:
                y = y * len(x)
            if len(x) == 1:
                x = x * len(y)
            ziplist = list(zip(x, y))
            for element in ziplist:
                newpoint = str(element[0])+":"+str(element[1])
                expanded_points.append(newpoint)
    return expanded_points


def expand_points_part2(points_list):
    """Part 2."""
    expanded_points_part2 = []

    for point_set in points_list:
        startx = point_set[0]
        starty = point_set[1]
        endx = point_set[2]
        endy = point_set[3]
        if startx <= endx:
            x = list(range(startx, endx+1))
        elif startx > endx:
            x = list(range(startx,endx-1,-1))
        elif startx == endx:
            x = [startx]

        if starty <= endy:
            y = list(range(starty, endy+1))
        elif starty > endy:
            y = list(range(starty,endy-1,-1))
        elif starty == endy:
            y = [starty]

        if len(y) == 1:
            y = y * len(x)
        if len(x) == 1:
            x = x * len(y)
        ziplist = list(zip(x, y))
        for element in ziplist:
            newpoint = str(element[0])+":"+str(element[1])
            expanded_points_part2.append(newpoint)
    return expanded_points_part2


def find_overlaps(expanded_points):
    count = 0
    point_count = Counter(expanded_points)
    multi_count = {key:val for key, val in point_count.items() if val > 1}
    return len(multi_count)


points =  load_lines_from_file("day5input.txt")
part1_expanded_points = expand_points_part1(points)
part1_solution = find_overlaps(part1_expanded_points)
print(part1_solution)

part2_expanded_points = expand_points_part2(points)
part2_solution = find_overlaps(part2_expanded_points)
print(part2_solution)
