from turtle import Turtle, Screen

tl = Turtle()
tl.shape("turtle")
for n in range(10):
    tl.forward(10)
    tl.penup()
    tl.forward(10)
    tl.pendown()

sc = Screen()
sc.exitonclick()