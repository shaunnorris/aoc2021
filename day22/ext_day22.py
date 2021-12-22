#full crdit to: https://gitlab.com/dos1/aoc21/-/blob/main/day22.py
#for this fairly clever solution
lines = [(line[0], [coord.split('=')[1] for coord in line[1].split(',')]) for line in [line.strip().split(' ') for line in open("day22input.txt")]]
lines = [(*[[*map(int,coord.split('..'))] for coord in line[1]], line[0] == "on") for line in lines]
def count(c): return 0 if c[0][0]>c[0][1] or c[1][0]>c[1][1] or c[2][0]>c[2][1] else (c[0][1]-c[0][0]+1)*(c[1][1]-c[1][0]+1)*(c[2][1]-c[2][0]+1)
def intersect(a, b): return tuple((max(a[x][0], b[x][0]), min(a[x][1], b[x][1])) for x in range(3))
cuboids = []; fivties = ((-50, 50), (-50, 50), (-50, 50))
for line in lines:
  intersections = [tuple([*intersect(cuboid, line), not cuboid[3]]) for cuboid in cuboids if count(intersect(line, cuboid))]
  cuboids += [line, *intersections] if line[3] else intersections
print(*(sum(count(transform(cuboid))*[-1,1][cuboid[3]] for cuboid in cuboids) for transform in [lambda x:intersect(x, fivties), lambda x:x]))
