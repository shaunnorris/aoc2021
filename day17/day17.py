def run_step(shot):
    newshot = {}
    newshot['target_x'] = shot['target_x']
    newshot['target_y'] = shot['target_y']
    newshot['x'] = shot['x'] + shot['x_vel']
    newshot['y'] = shot['y'] + shot['y_vel']
    if shot['x_vel'] >= 1:
        newshot['x_vel'] = shot['x_vel'] -1
    elif shot['x_vel'] >= -1:
        newshot['x_vel'] = 0
    else:
        newshot['x_vel'] = shot['x_vel'] + 1
    newshot['y_vel'] = shot['y_vel'] - 1
    return newshot

def fire_shot(shot):
    extent_x = shot['target_x'][1]
    extent_y = shot['target_y'][1]
    myshot = shot
    max_y = 0
    within_range = True
    target_hit = False
    while within_range and not target_hit:
        myshot = run_step(myshot)
        if myshot['y'] > max_y:
            max_y = myshot['y']
        within_range = in_range(myshot)
        target_hit = on_target(myshot)
    return target_hit, max_y

def in_range(myshot):
    x = myshot['x']
    y = myshot['y']
    x_range = myshot['target_x']
    y_range = myshot['target_y']
    if x <= x_range[1]:
        if y >= y_range[0]:
            return True
    return False

def on_target(myshot):
    x = myshot['x']
    y = myshot['y']
    x_range = myshot['target_x']
    y_range = myshot['target_y']
    if x >= x_range[0] and x <= x_range[1]:
        if y >= y_range[0] and y <= y_range[1]:
            #print("x and y on target",x,y)
            return True
    return False

def all_shots(target):
    max_height = 0
    targets_hit = 0
    myshot = {}
    myshot['x'] = 0
    myshot['y'] = 0
    myshot['target_x'] = target[0]
    myshot['target_y'] = target[1]
    for x_vel in range(0,target[0][1]+1):
        for y_vel in range(target[1][0],abs(target[1][0])+1):
            myshot['x_vel'] = x_vel
            myshot['y_vel'] = y_vel
            testshot = fire_shot(myshot)
            if testshot[0]:
                targets_hit += 1
                if testshot[1] > max_height:
                    max_height = testshot[1]
    #print("max height for all shots:", max_height)
    return max_height, targets_hit

#raw_input = "target area: x=201..230, y=-99..-65"
target_x = (201,230)
target_y = (-99,-65)
puzzle = all_shots([target_x, target_y])
print("part1:", puzzle[0])
print("part2:", puzzle[1])
