import turtle as t
import random
dir = [0,90,180,270]

tim = t.Turtle()
t.colormode(255)
t.speed("fastest")
tim.pensize(15)


def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)

for n in range(200):
    tim.color(random_color())
    tim.forward(50)
    tim.setheading(random.choice(dir))

my_screen = t.Screen()
my_screen.exitonclick()