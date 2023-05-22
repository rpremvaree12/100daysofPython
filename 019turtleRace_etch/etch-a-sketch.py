from turtle import Turtle, Screen

don = Turtle()
screen = Screen()

screen.listen()


def move_forward():
    don.forward(10)

def move_backward():
    don.backward(10)

def turn_left():
    don.setheading(don.heading() - 10)

def turn_right():
    don.setheading(don.heading() + 10)

def clear_screen():
    screen.resetscreen()

screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear_screen)

screen.exitonclick()