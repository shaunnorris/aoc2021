from day24 import *

example_file = "test_day24input.txt"
example_list = load_file(example_file)
main_list = load_file("day24input.txt")

expected_list = []

def test_file_load():
    assert example_list[-1] == 'mod w 2'
    assert len(example_list) == 11

def test_alu_inputs():
    test_alu = alu()
    test_alu.inp('x', 11)
    assert test_alu.get('x') == 11
    test_alu.inp('w', 99)
    assert test_alu.get('w') == 99

def test_alu_add():
    test_alu = alu()
    test_alu.inp('x', 11)
    test_alu.inp('y', 9)
    assert test_alu.add('x','y') == 20
    assert test_alu.add('w', 1) == 1
    assert test_alu.add('y', 1) == 10
    assert test_alu.add('y', 'z') == 10

def test_alu_mul():
    test_alu = alu()
    test_alu.inp('x', 10)
    test_alu.inp('y', 5)
    test_alu.inp('z', 3)
    test_alu.inp('w', 2)
    assert test_alu.mul('x',10) == 100 
    assert test_alu.mul('x','y') == 500 
    assert test_alu.mul('z','w') == 6 

def test_alu_div():
    test_alu = alu()
    test_alu.inp('x', '10')
    test_alu.inp('y', 5)
    test_alu.inp('z', 3)
    test_alu.inp('w', 2)
    assert test_alu.div('x','y') == 2
    assert test_alu.div('x',0) == False
    assert test_alu.div('x',2) == 1
    assert test_alu.div('z',2) == 1
    test_alu.inp('x', 9)
    assert test_alu.div('x',10) == 0

def test_alu_mod():
    test_alu = alu()
    test_alu.inp('x', 10)
    test_alu.inp('y', 5)
    test_alu.inp('z', 3)
    test_alu.inp('w', 2)
    assert test_alu.mod('x','y') == 0
    assert test_alu.mod('y',2) == 1
    test_alu.inp('x', 42)
    assert test_alu.mod('x', 41) == 1

def test_alu_eql():
    test_alu = alu()
    test_alu.inp('x', 10)
    test_alu.inp('y', 10)
    test_alu.inp('z', 3)
    test_alu.inp('w', 2)
    assert test_alu.eql('x','y') == 1
    assert test_alu.eql('y','z') == 0
    assert test_alu.eql('w', 2) == 1

def test_binary_convert():
    program = example_list
    assert binary_convert(program, 15) == (1,1,1,1)
    assert binary_convert(program, 1) == (0,0,0,1)
    assert binary_convert(program, 7) == (0,1,1,1)

def test_monad():
    program = main_list
    assert monad(program, '13579246899999') == 0