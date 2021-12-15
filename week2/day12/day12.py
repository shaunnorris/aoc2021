def load_file(filename):
    with open(filename) as f:
        mylist = f.read().splitlines()
    return mylist


def build_graph(mylist):
    graph = {}
    for entry in mylist:
        points = entry.split('-')
        if points[0] in graph:
            graph[points[0]].append(points[1])
        else:
            graph[points[0]] = [points[1]]
        if points[1] in graph:
            graph[points[1]].append(points[0])
        else:
            graph[points[1]] = [points[0]]
    return graph


def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return []
    paths = []
    for node in graph[start]:
        if node not in path or node.isupper():
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths

def find_all_paths_pt2(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return []
    paths = []
    for node in graph[start]:
        if node not in path or node.isupper() or no_repeated_lower(node, path):
            newpaths = find_all_paths_pt2(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths

def no_repeated_lower(node, path):
    if node == 'start':
        return False
    for node in path:
        if node.islower():
            if path.count(node) > 1:
                return False
    return True



input_file = "day12input.txt"
input_list = load_file(input_file)
part1_graph = build_graph(input_list)
part1 = len(find_all_paths(part1_graph,'start','end'))
print(part1)
part2 = len(find_all_paths_pt2(part1_graph,'start','end'))
print(part2)
