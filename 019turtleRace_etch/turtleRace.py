from turtle import Turtle, Screen
import random

screen = Screen()
screen.bgcolor("black")
screen.setup(width=500,height=500)
colors = ["red","orange","yellow","green","blue","indigo","violet"]
turtles = []
bet = screen.textinput(title="Place your bet",prompt=f"Which color turtle do you think will win? {colors}")

for i in range(len(colors)):
    turtles.append(Turtle("turtle"))
    turtles[i].penup()
    turtles[i].color(colors[i])
    turtles[i].goto(x=-230, y=-100 + i*30)
    
screen.listen()

is_race_on = False
if bet:
    is_race_on = True

while is_race_on:
    for t in turtles:
        t.forward(random.randint(0,10))
        if t.xcor() > 230:
            is_race_on = False
            winning_turtle = t.pencolor()
            if winning_turtle == bet:
                print(f"You've won! {winning_turtle.title()} turtle was the winning turtle!")
            else:
                print(f"Sorry. You've lost. {winning_turtle.title()} turtle was the winning turtle.")
            break
            
            


screen.exitonclick()