#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json

def turn_right():
    for n in range(0,3):
        turn_left()
def jump():
    turn_right()
    move()
    turn_right()
    move()

while not at_goal():
    if wall_on_right() and wall_in_front():
        turn_left()
    elif wall_on_right():
        move()
        if right_is_clear():
            jump()       