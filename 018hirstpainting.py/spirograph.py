import turtle as t
import random
# turtle.colormode(255)

tim = t.Turtle()
t.colormode(255)
# tim.pensize(15)
tim.speed("fastest")
my_screen = t.Screen()
directions = [0,90,180,270]

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)

def draw_spirograph(size_of_gap):
    """size of gap  is in degrees - how much to rotate in between"""
    for i in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(random.randint(100,200))
        tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(2)
my_screen.exitonclick()