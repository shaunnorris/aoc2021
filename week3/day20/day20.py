def load_file(filename):
    myinput = {}
    with open(filename) as f:
        mylist = f.read().splitlines()
    myinput['algo'] = mylist[0]
    rawpic = mylist[2:]
    #pad image with dark cells to simulate infinity
    myinput['pic'] = pad_pic(rawpic,'.')
    return myinput

def pad_pic(pic, char):
    for i in range(len(pic)):
        pic[i] =  char * 3 + pic[i]+ char * 3
    s = char * len(pic[0])
    padlist = [s,s,s]
    newpic = padlist + pic + padlist
    #print("padded",len(newpic),len(newpic[0]))
    return newpic

def get_index(pic, x, y):
    numstring = ''
    offsets = [(x-1,y-1),(x-1,y),(x-1,y+1),
                (x,y-1),(x,y),(x,y+1),
                (x+1,y-1),(x+1,y),(x+1,y+1)]
    for a,b in offsets:
        #print("a,b",a,b)
        numstring += pic[a][b]
    #print("numstring:",numstring)
    numstring = numstring.replace(".","0")
    numstring = numstring.replace("#","1")
    #print("numstring:",numstring)
    return int(numstring ,2)

def enhance(mydict):
    pic = mydict['pic']
    algo = mydict['algo']
    output = []
    #print("piclength",len(pic))
    infi_str = algo[get_index(pic,1,1)]
    #print("infi-str:",infi_str)
    for i in range(0,len(pic)):
        pixelstring = ''
        for j in range(0,len(pic[0])):
            #print("i,j:",i,j)
            if i == 0 or i == len(pic)-1:
                pixel = infi_str
            elif j == 0 or j == len(pic[0])-1:
                pixel = infi_str
            else:
                pixel = algo[get_index(pic, i, j)]
            pixelstring += pixel
        output.append(pixelstring)
    #print("i:j",i,j)
    #print("enhanced output",len(output),len(output[0]))
    return output, hashcount(output)

def hashcount(pic):
    hashcount = 0
    for line in pic:
        hashcount += line.count('#')
    #print("hashcount",hashcount)
    return hashcount

def print_pic(pic):
    for line in pic:
        print(line)

def crop_pic(pic,pixels):
    newpic = []
    for line in pic:
        newline = line[pixels:len(line)-(pixels)]
        newpic.append(newline)
    newpic = newpic[pixels:len(newpic)-pixels]
    return newpic

def enhance_n_times(picdict, times):
    inputpic = picdict['pic']
    algo = picdict['algo']
    for run in range(times):
        inputdict = {'pic': inputpic, 'algo': algo}
        #print("run",run)
        outputpic = enhance(inputdict)
        newpic = outputpic[0]
        #print("picsize",len(newpic),len(newpic[0]))
        pad_str = newpic[0][1]
        newpic = pad_pic(newpic, pad_str)
        inputpic = newpic
    return hashcount(newpic)

puzzle_input = "day20input.txt"

input = load_file(puzzle_input)
print("part1:",enhance_n_times(input, 2))

print("part2:",enhance_n_times(input, 50))
