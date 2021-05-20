import turtle as t
import random
tim = t.Turtle()
ColorList = ["snow", "salmon", "pale turquoise", "lime green", "sandy brown"]
def DrawShape(sides):
    for i in range(sides):
        angle=360/sides
        tim.forward(100)
        tim.right(angle)
for i in range(3,11):
    tim.color(random.choice(ColorList))
    DrawShape(i)
scr=t.Screen()
scr.exitonclick()