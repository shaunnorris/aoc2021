def load_file(filename):
    with open(filename) as f:
        lines = f.readlines()
    raw_list = lines[0].split(',')
    start_list = [int(x) for x in raw_list]
    return start_list


def find_best_position(position_list):
    best_fuel = 999999
    best_pos = -99
    for test_pos in range(min(position_list), max(position_list)+1):
        total_fuel = 0
        for actual_pos in position_list:
            fuel = abs(actual_pos - test_pos)
            total_fuel = total_fuel + fuel
        if total_fuel < best_fuel:
            best_fuel = total_fuel
            best_pos = test_pos
    return best_fuel

def find_best_part2_position(position_list):
    best_fuel = 999999999
    best_pos = -99
    for test_pos in range(min(position_list), max(position_list)+1):
        total_fuel = 0
        for actual_pos in position_list:
            fuel = 0
            difference = abs(test_pos - actual_pos)
            fuel = sum(range(difference +1))
            total_fuel = total_fuel + fuel
        if total_fuel < best_fuel:
            best_fuel = total_fuel
            best_pos = test_pos
    return best_fuel



file = "day7input.txt"
position_list = load_file(file)
part1 = find_best_position(position_list)
print(part1)
part2 = find_best_part2_position(position_list)
print(part2)
