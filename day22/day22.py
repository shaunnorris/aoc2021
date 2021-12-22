def load_file(filename):
    with open(filename) as f:
        mylist = f.read().splitlines()
    return mylist


def read_instruction(instruction):
    mydict = {}
    first = instruction.split(' ')
    mydict['onoff'] = first[0]
    xyz = first[1].split(',')
    for coord in xyz:
        elements = coord.split('=')
        axis = elements[0]
        startrange = int(elements[1].split('..')[0])
        endrange = int(elements[1].split('..')[1])
        if startrange > 50 or startrange < -50:
            mydict['onoff'] = 'oor'
        if endrange > 50 or endrange < -50:
            mydict['onoff'] = 'oor'
        mydict[axis] = list(range(startrange,endrange+1))
    return mydict


def initialise(mylist):
    pointson = []
    for line in mylist:
        ins = read_instruction(line)
        subset = []
        for x in ins['x']:
            for y in ins['y']:
                for z in ins['z']:
                    pointstring = 'x'+str(x)+'y'+str(y)+'z'+str(z)
                    print("pointstring",pointstring)
                    subset.append(pointstring)
        if ins['onoff'] == 'on':
            pointson.extend(x for x in subset if x not in pointson)
        elif ins['onoff'] == 'off':
            for point in subset:
                if point in pointson:
                    pointson.remove(point)
    print(pointson)
    return len(pointson)

#puzzle_input = load_file("test_day22input.txt")
#output = initialise(puzzle_input)
#print("output:",output)
