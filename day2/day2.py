def pos_by_depth(input_list):
    horizontal = 0
    depth = 0
    for command in input_list:
        move = command.split()[0].strip()
        quantity = int(command.split()[1])
        if move == "forward":
            horizontal += quantity
        elif move == "down":
            depth += quantity
        elif move == "up":
            depth -= quantity
    return horizontal * depth


def pos_by_depth_complex(input_list):
    aim = 0
    horizontal = 0
    depth = 0
    for command in input_list:
        move = command.split()[0].strip()
        quantity = int(command.split()[1])
        if move == "forward":
            horizontal += quantity
            depth += (aim * quantity)
        elif move == "down":
            aim += quantity
        elif move == "up":
            aim -= quantity
    return horizontal * depth


file = "input.txt"
with open(file) as f:
    lines = f.readlines()
inputlist = []
for line in lines:
    inputlist.append(line.strip())\

part1 = pos_by_depth(inputlist)
print(part1)
part2 = pos_by_depth_complex(inputlist)
print(part2)
