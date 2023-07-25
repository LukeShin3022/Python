import turtle as t

tur = t.Turtle()
colors =["red","blue","green"]
def draw_shape(num_sides):
    angle = 360 / num_sides
    for n in range(num_sides):
        tur.forward(100)
        tur.right(angle)



for n in range(3,30):
    tur.pencolor(colors[n%3])
    draw_shape(n)


scr = t.Screen()
scr.exitonclick()