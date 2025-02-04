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
    
def wall_logic():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    
while not at_goal():
    if wall_in_front() == True:
        wall_logic()
        turn_left()
    elif at_goal() == True:
        break
    elif front_is_clear():
        move()
    

    