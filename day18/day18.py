def load_file(filename):
    with open(filename) as f:
        mylist = f.read().splitlines()
    return mylist

def find_explode(mylist):
    explode = ''

    def listwalk(sublist,depth=0):
        print("sublist, depth",sublist,depth)
        if depth == 4 and isinstance(sublist, list):
            explode = sublist
        while len(sublist) > 0:
            element = sublist.pop()
            if isinstance(element, list):
                return listwalk(element,depth+1)

    return listwalk(mylist)





puzzle_input = load_file("day18input.txt")
