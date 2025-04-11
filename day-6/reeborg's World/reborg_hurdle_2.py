def turn_right():
    turn_left()
    turn_left()
    turn_left()

def hurdle_2():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
rotation = 6
while rotation > 0:
    hurdle_2()
    if at_goal()==True:
        break
    else:
        rotation -=1