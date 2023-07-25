from turtle import Turtle, Screen

turtle = Turtle()

# turtle.penup()
# turtle.setpos(100,100)
# turtle.pendown()
# turtle.fd(50)
# turtle.lt(90)
# turtle.fd(50)
# turtle.lt(90)
# turtle.fd(50)
# turtle.lt(90)
# turtle.fd(50)

for n in range(4):
    turtle.fd(50)
    turtle.lt(90)

screen = Screen()
screen.exitonclick()
