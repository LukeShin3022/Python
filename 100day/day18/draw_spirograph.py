import random
import turtle as t

t.colormode(255)
tim = t.Turtle()
tim.speed(0)
tim.pensize(3)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

# for n in range(72):
#     tim.color(random_color())
#     tim.circle(100)
#     tim.right(5)

for n in range(36):
    tim.color(random_color())
    tim.circle(100)
    current_heading = tim.heading()
    tim.setheading(current_heading + 10)

screen = t.Screen()
screen.exitonclick()