from turtle import Turtle, Screen
import time

#TODO: fix game

screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
# won't show until we update the screen
screen.tracer(0)
screen.title("My Snake Game")

snake_body = []
def game_start():
    for i in range(3):
        snake_body.append(Turtle("square"))
        snake_body[i].penup()
        snake_body[i].color("white")
        snake_body[i].goto(0+i*-20,0)
    screen.update()

def move_forward():
    for t in snake_body:
        t.forward(20)

def check_wall():
    for t in snake_body:
        if t.xcor() > 230:
            return True

game_start()
screen.listen()
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(1)
    move_forward()
    if check_wall():
        game_is_on = False
screen.onkey(key="w",fun=move_forward)
screen.exitonclick()

