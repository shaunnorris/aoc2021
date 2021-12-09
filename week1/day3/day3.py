def find_most_common(input_list, i):
    """i is the position index."""
    zerocount = 0
    onecount = 0
    for input in input_list:
        if input[i] == "0":
            zerocount += 1
        elif input[i] == "1":
            onecount += 1
    if onecount >= zerocount:
        return True
    else:
        return False

def find_sub_common_list(input_list, highlow):
    accumulated_list = []
    complement_list = []
    for i in range(0, len(input_list[0])):
        if find_most_common(input_list, i):
            accumulated_list.append("1")
            complement_list.append("0")
        else:
            accumulated_list.append("0")
            complement_list.append("1")
    if highlow == 1:
        return accumulated_list
    elif highlow == 0:
        return complement_list


def find_sub_power(input_list):
    accumulated_list = find_sub_common_list(input_list, 1)
    complement_list = find_sub_common_list(input_list, 0)
    decmost = int(''.join(accumulated_list), 2)
    decleast = int(''.join(complement_list), 2)
    return decmost * decleast

def find_sub_ox_rating(input_list):
    treelist = {}
    treelist[0] = input_list
    for i in range(0, len(input_list[0])):
        newlist = []
        if find_most_common(treelist[i], i):
            keeper = "1"
        else:
            keeper = "0"
        for input in treelist[i]:
            if input[i] == keeper:
                newlist.append(input)
            treelist[i+1] = newlist
        if len(newlist) == 1:
            return int(''.join(newlist), 2)

def find_sub_co2_rating(input_list):
    treelist = {}
    treelist[0] = input_list
    for i in range(0, len(input_list[0])):
        newlist = []
        if not find_most_common(treelist[i], i):
            keeper = "1"
        else:
            keeper = "0"
        for input in treelist[i]:
            if input[i] == keeper:
                newlist.append(input)
            treelist[i+1] = newlist
        if len(newlist) == 1:
            return int(''.join(newlist), 2)

def find_sub_lifesupport(input_list):
    return find_sub_co2_rating(input_list) * find_sub_ox_rating(input_list)


file = "day3input.txt"
with open(file) as f:
    lines = f.readlines()
inputlist = []
for line in lines:
    inputlist.append(line.strip())

part1 = find_sub_power(inputlist)
print(part1)
part2 = find_sub_lifesupport(inputlist)
print(part2)
