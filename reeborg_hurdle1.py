def turn_right():
    turn_left()
    turn_left()
    turn_left()
def step_function():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
for i in range(0,6):
    step_function()