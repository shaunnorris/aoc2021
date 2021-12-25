def load_file(filename):
    with open(filename) as f:
        mylist = f.read().splitlines()
    return mylist


def move_herd(mylist):
    
 
    newlist = []
    rightlist = []
    downlist = []
    
    for x in range(len(mylist)):
        for y in range(len(mylist[0])):
            if mylist[x][y] == '>':
                rightlist.append((x,y))
            elif mylist[x][y] == 'v':
                downlist.append((x,y))

    animal = '>'    #print("animal now:",animal)
    for x, row in enumerate(mylist):
        for y, element in enumerate(row):
            if element == animal:
                mymove = is_empty(mylist, x, y)
                if mymove[0] == True:
                    rightlist.remove((x, y))
                    rightlist.append((mymove[1],mymove[2]))

    for x in range(len(mylist)):
        newline = ''
        for y in range(len(mylist[0])):   
            if (x, y) in downlist:
                newline = newline + 'v' 
            elif (x, y) in rightlist:
                newline = newline + '>'
            else:
                newline = newline + '.'          
        newlist.append(newline)      
    
    mylist = newlist
    newlist = []

    animal = 'v'    #print("animal now:",animal)
    for x, row in enumerate(mylist):
        for y, element in enumerate(row):
            if element == animal:
                mymove = is_empty(mylist, x, y)
                if mymove[0] == True:
                    downlist.append((mymove[1],mymove[2]))
                    downlist.remove((x, y))
    
    for x in range(len(mylist)):
        newline = ''
        for y in range(len(mylist[0])):
          
            if (x, y) in downlist:
                newline = newline + 'v' 
            elif (x, y) in rightlist:
                newline = newline + '>'
            else:
                newline = newline + '.'          
        newlist.append(newline)
    
    
    return newlist

def is_empty(mylist, x, y):
    animal = mylist[x][y]
    #print("animal,x,y",animal,x,y)
        
    if animal == ">":
        targetx = x
        if y < len(mylist[0])-1:
            targety = y+1
        else:
            targety = 0

    elif animal == "v":
        targety = y
        if x < len(mylist)-1:
            targetx = x+1
        else:
            targetx = 0
    else:
        return "Error not an animal"
    
    if mylist[targetx][targety] == '.':
        #print(animal, "can move from",x,y," to ",targetx,targety)
        return True, targetx, targety
    else:
        #print(animal,"cant move from",x,y)
        return False, x, y


def find_no_moves(mylist):
    count = 1
    moving = True
    inputlist = mylist
    while moving: 
        outputlist = move_herd(inputlist)
        if outputlist == inputlist:
            moving = False
        else:
            inputlist = outputlist
            count +=1
            print("count:",count)
    return count


puzzle_input = load_file("day25input.txt")
part1 = find_no_moves(puzzle_input)
print("part1:",part1)