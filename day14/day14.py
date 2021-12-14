from collections import Counter

def load_file(filename):
    with open(filename) as f:
        mylist = f.read().splitlines()
    pairmap = {}
    rootsequence = ""
    for entry in mylist:
        if "->" in entry:
            pair = entry.split('->')
            pairmap[pair[0].strip()] = pair[1].strip()
        else:
            if len(entry) > 1:
                rootsequence = entry
    return [pairmap, rootsequence]

def insert_pairs(mymap, root_sequence):
    new_sequence = ""
    for i in range(len(root_sequence) -1):
        check_pair = root_sequence[i:i+2]
        if check_pair in mymap.keys():
            newpair = check_pair[0] + mymap[check_pair]
            new_sequence += newpair
        else:
            new_sequence += check_pair[0]
    new_sequence += root_sequence[-1]
    return new_sequence

def count_pairs(mymap, root_map):
    new_map = {}
    for parent, count in root_map.items():
        for key, value in mymap.items():
            firstpair = key[0] + value
            secondpair = value + key[1]
            if key == parent:
                if firstpair in new_map:
                    new_map[firstpair] += count
                else:
                    new_map[firstpair] = count
                if secondpair in new_map:
                    new_map[secondpair] += count
                else:
                    new_map[secondpair] = count

    return new_map

def count_elements(mymap, first, last):
    single_map = {}
    for key, count in mymap.items():
        for element in key:
            if element in single_map:
                single_map[element] += count
            else:
                single_map[element] = count
    single_map[first] += 1
    single_map[last] += 1
    for element, count in single_map.items():
        single_map[element] = int(count / 2)
    return single_map

def multi_map(mymap, root_sequence, rounds):
    root_map = {}
    for i in range(len(root_sequence)-1):
        pair = root_sequence[i:i+2]
        if pair in root_map:
            root_map[pair] += 1
        else:
            root_map[pair] = 1
    first = root_sequence[0]
    last = root_sequence[-1]
    polymer_count = root_map
    for i in range(rounds):
        new_polymer_count = count_pairs(mymap, polymer_count)
        polymer_count = new_polymer_count
    score = count_elements(polymer_count, first, last)
    score_max = score[max(score.keys(), key=(lambda k: score[k]))]
    score_min = score[min(score.keys(), key=(lambda k: score[k]))]
    return score_max - score_min



puzzle_input = load_file("day14input.txt")
pairmap = puzzle_input[0]
root_sequence = puzzle_input[1]
part1 = multi_map(pairmap, root_sequence, 10)
print(part1)
part2 = multi_map(pairmap, root_sequence, 40)
print(part2)
