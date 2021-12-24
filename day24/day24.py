def load_file(filename):
    with open(filename) as f:
        mylist = f.read().splitlines()
    return mylist


class alu(object):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 0
        self.w = 0

    def inp(self, variable, value):
        if variable == 'x':
            self.x = int(value)
        elif variable == 'y':
            self.y = int(value)
        elif variable == 'z':
            self.z = int(value)
        elif variable == 'w':
            self.w = int(value)

    def get(self, variable):
        if variable == 'x':
           return self.x
        elif variable == 'y':
            return self.y
        elif variable == 'z':
            return self.z
        elif variable == 'w':
            return self.w

    def add(self, a, b):
        current_val = self.get(a)
        if b in ['x','y','z','w']:
            add_val = self.get(b)
        else:
            add_val = int(b)
        self.inp(a, current_val + add_val)
        return current_val + add_val
    
    def mul(self, a, b):
        current_val = self.get(a)
        if b in ['x','y','z','w']:
            add_val = self.get(b)
        else:
            add_val = int(b)
        self.inp(a, current_val * add_val)
        return current_val * add_val

    def div(self, a, b):
        current_val = self.get(a)
        if b in ['x','y','z','w']:
            print("b is variable",b)
            add_val = self.get(b)
        else:
            add_val = int(b)
        if add_val != 0:
            self.inp(a, current_val // add_val)
            return current_val // add_val
        else: 
            return False
    
    def mod(self, a, b):
        current_val = self.get(a)
        if b in ['x','y','z','w']:
            add_val = self.get(b)
        else:
            add_val = int(b)
        if add_val != 0:
            self.inp(a, current_val % add_val)
            return current_val % add_val
        else: 
            return False
        
    def eql(self, a, b):
        current_val = self.get(a)
        if b in ['x','y','z','w']:
            add_val = self.get(b)
        else:
            add_val = int(b)
        if current_val == add_val:
            self.inp(a, 1)
            return 1
        else: 
            self.inp(a, 0)
            return 0

def binary_convert(myprogram, myinput):
    cpu = alu()
    for line in myprogram: 
        code = line.split(' ')
        print(code)
        if code[0] == 'inp':
            cpu.inp(code[1], myinput)
        elif code[0] == 'add':
            cpu.add(code[1], code[2])
        elif code[0] == 'div':
            cpu.div(code[1], code[2])
        elif code[0] == 'mod':
            cpu.mod(code[1], code[2])
        elif code[0] == 'mul':
            cpu.mul(code[1], code[2])
        elif code[0] == 'eql':
            cpu.eql(code[1], code[2])
    #print("w,x,y,z:",cpu.get('w'),cpu.get('x'),cpu.get('y'),cpu.get('z'))
    return cpu.get('w'),cpu.get('x'),cpu.get('y'),cpu.get('z')

def monad(myprogram, myinput):
    digit_string = str(myinput)
    digit_map = map(int, digit_string)
    digit_list = list(digit_map)
    
    cpu = alu()
    for line in myprogram: 
        code = line.split(' ')
        #print(code)
        if code[0] == 'inp':
            cpu.inp(code[1], digit_list.pop(0))
        elif code[0] == 'add':
            cpu.add(code[1], code[2])
        elif code[0] == 'div':
            cpu.div(code[1], code[2])
        elif code[0] == 'mod':
            cpu.mod(code[1], code[2])
        elif code[0] == 'mul':
            cpu.mul(code[1], code[2])
        elif code[0] == 'eql':
            cpu.eql(code[1], code[2])
        print("code:",code)
        print("w,x,y,z:",cpu.get('w'),cpu.get('x'),cpu.get('y'),cpu.get('z'))
    return cpu.get('z')

def try_model_numbers(myprogram):
    current_num = "99999999999999"
    found_valid = False
    while not found_valid:
        digit_string = str(current_num)
        if '0' not in digit_string:
            test = monad(myprogram, current_num)
            if test == 0:
                found_valid = True
                return current_num
        current_num = int(current_num) - 1
    
#puzzle_input = load_file("day24input.txt")
#part1 = try_model_numbers(puzzle_input)
#print(part1)