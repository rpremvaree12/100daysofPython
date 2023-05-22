from turtle import Turtle, Screen

don = Turtle()
screen = Screen()

def move_forward():
    don.forward(10)

# event listener
screen.listen()

# event listener for key press. no () because we want it to execute when the key is pressed.
# () triggers the function right there and then
screen.onkey(key="space", fun=move_forward)

screen.exitonclick()


# calculator with higher order function
def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def mul(n1,n2):
    return n1*n2
def div(n1,n2):
    return n1/n2

def calculator(n1,n2,func):
    return func(n1,n2)

print(calculator(1,2,add))