"""Day1 aoc implementation code."""

def find_increases(depth_list):
    """Find consecutive increases in a list."""
    increase_count = 0
    for index in range(1, len(depth_list)):
        current = int(depth_list[index])
        previous = int(depth_list[index-1])
        if current > previous:
            increase_count += 1
    return increase_count


def find_3way_increases(d_l):
    """Find increases in 3 number runs - AOC day1 part2."""
    increase_count = 0
    for index in range(3, len(d_l)):
        previous_sum = d_l[index-3] + d_l[index-2] + d_l[index-1]
        current_sum = d_l[index-2] + d_l[index-1] + d_l[index]
        if current_sum > previous_sum:
            increase_count += 1
    return increase_count


file = ROOT_DIR + "/day1/day1input.txt"
with open(file) as f:
    lines = f.readlines()
day1inputlist = []
for line in lines:
    day1inputlist.append(int(line.strip()))

part1 = find_increases(day1inputlist)
print(part1)
part2 = find_3way_increases(day1inputlist)
print(part2)
