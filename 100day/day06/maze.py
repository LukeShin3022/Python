#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json


def turn_right():
    for n in range(0,3):
        turn_left()
while front_is_clear():
    move()
turn_left()
        
while not at_goal():
    while (front_is_clear() and wall_on_right()) or front_is_clear():
        move()          
        if right_is_clear() and front_is_clear():
            turn_right()
    if wall_in_front() and wall_on_right():
        turn_left()
    elif wall_in_front() and right_is_clear():
        turn_right()