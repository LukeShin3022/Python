import turtle as t
import random

tim = t.Turtle()
scr = t.Screen()
t.colormode(255)
# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [0,90,180,270]
tim.pensize(10)
tim.speed(0)
def rgb_color():
    random_color = ()
    for n in range(3):
        random_color = random_color + (random.randrange(0,256), )
    return random_color

for n in range(100):
    colours = rgb_color()
    tim.color(colours)
    # tim.color(rgb_color())
    tim.forward(50)
    tim.setheading(random.choice(directions))


scr.exitonclick()
