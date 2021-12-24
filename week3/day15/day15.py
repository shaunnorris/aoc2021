def load_file(filename):
    matrix = []
    with open(filename) as f:
        linelist = f.read().splitlines()
    for line in linelist:
        newrow = []
        for char in line:
            newrow.append(int(char))
        matrix.append(newrow)
    return matrix


def build_graph(matrix):
    graph = {}
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            graph[(x,y)] = {}
            for offset in [(-1,0),(1,0),(0,-1),(0,1)]:
                target = (offset[0] + x, offset[1] + y)
                if target[0] >=0 and target[0] < len(matrix):
                    if target[1] >=0 and target[1] < len(matrix[0]):
                        graph[(x,y)][target] = matrix[target[0]][target[1]]

    return graph


def find_path(graph):
    shortest_path = []
    visited = []
    shortest_path.append([(0,0)])
    distances = {}
    for key in graph:
        distances[key] = float('inf')
    distances[(0,0)] = 0
    print(distances)
    workqueue = []
    workqueue.append((0,0))
    while distances[(2,2)] == float('inf'):
        for vertex in workqueue:
            print("-------------")
            print("vertex",vertex)
            visited.append(vertex)
            print("visited",visited)
            print("distances",distances)
            new_vertices = graph[vertex]
            current_distance = distances[vertex]
            shortest = ((0,0),float('inf'))
            for new_vertex, distance in new_vertices.items():
                print("newvertex,distance",new_vertex, distance)
                if new_vertex not in visited:
                    if distance < shortest[1]:
                        shortest = (new_vertex, distance)
                    if distance + current_distance < distances[new_vertex]:
                        distances[new_vertex] = distance + current_distance
                        workqueue.append(new_vertex)
            shortest_path.append((shortest))
            workqueue.pop()
    print(shortest_path)
    return False
