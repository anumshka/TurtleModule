import turtle as t
import random

scr = t.Screen()
scr.setup(width=500, height=500)
UserInput = scr.textinput(title="Play luck",
                          prompt="Who would win in your opinion??Enter your lucky color from rainbow")
ColorList = ["Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet"]
RaceRunning = False
Runners = []
pos = -100
for i in range(0, 7):
    NewTurtle = t.Turtle()
    NewTurtle.shape("turtle")
    NewTurtle.penup()
    NewTurtle.color(ColorList[i])
    NewTurtle.goto(x=-250, y=pos)
    pos += 50
    Runners.append(NewTurtle)
if UserInput:
    RaceRunning = True
while RaceRunning == True:
    for runner in Runners:
        if runner.xcor() > 230:
            winner = runner.pencolor()
            RaceRunning = False
            if winner == UserInput:
                print("Your turtle won!")
            else:
                print(f"Your turtle lost, the winner is {winner} turtle!")
        runner.forward(random.randint(0, 10))
scr.exitonclick()
