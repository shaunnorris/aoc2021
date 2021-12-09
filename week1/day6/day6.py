from collections import Counter

def load_file(filename):
    with open(filename) as f:
        lines = f.readlines()
    raw_list = lines[0].split(',')
    start_list = [int(x) for x in raw_list]
    return start_list


def simulate_day(startlist, days):
    """ugly slow way to simulate."""
    yesterday_list = startlist
    for day in range(1,days+1):
        today_list = []
        zerocount = 0
        for fish in yesterday_list:
            if fish > 0:
                today_list.append(fish-1)
            elif fish == 0:
                zerocount +=1
                today_list.append(6)
        #add 8's at end for each zero encountered
        for q in range(0,zerocount):
            today_list.append(8)
        yesterday_list = today_list
    return len(today_list)

def map_day(startlist, days):
    """map the number of each fish to a dict xxxxx faster."""
    yesterday_dict = dict(Counter(startlist))
    for day in range(1,days+1):
        today_dict = {}
        for number in yesterday_dict:
            if number > 0:
                today_dict[number-1] = yesterday_dict[number]
            elif number == 0:
                today_dict[8] = yesterday_dict[0]

        if 0 in yesterday_dict.keys():
            if 6 in today_dict.keys():
                today_dict[6] = today_dict[6] + yesterday_dict[0]
            else:
                today_dict[6] = yesterday_dict[0]

        yesterday_dict = today_dict
    return sum(today_dict.values())

file = "day6input.txt"
day0_list = load_file(file)
part1 = map_day(day0_list, 80)
print(part1)
part2 = map_day(day0_list, 256)
print(part2)
