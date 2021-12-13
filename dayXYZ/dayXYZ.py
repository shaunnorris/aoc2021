def load_file(filename):
    with open(filename) as f:
        mylist = f.read().splitlines()
    return mylist






puzzle_input = load_file("dayXYZinput.txt")
