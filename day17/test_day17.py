from day17 import *



expected_raw_input = "target area: x=20..30, y=-10..-5"
shot = {}
shot['x'] = 0
shot['y'] = 0
shot['x_vel'] = 7
shot['y_vel'] = 2
shot['target_x'] = (20,30)
shot['target_y'] = (-10,-5)

def test_run_step():
    step = run_step(shot)
    assert step['x'] == 7
    assert step['y'] == 2
    assert step['x_vel'] == 6
    assert step['y_vel'] == 1


def test_on_target():
    myshot = {}
    myshot['x'] = 30
    myshot['y'] = -5
    myshot['x_vel'] = 7
    myshot['y_vel'] = 2
    myshot['target_x'] = (20,30)
    myshot['target_y'] = (-10,-5)
    assert on_target(myshot) == True

def test_fire_shot():
    assert fire_shot(shot) == (True, 3)

def test_all_shots():
    assert all_shots([(20,30), (-10,-5)]) == (45,999)
