from turtle import Turtle, Screen
# import turtle
# timmy = turtle.Turtle()
# create an object of the Turtle class


timmy = Turtle()
timmy.shape("turtle")
timmy.color("coral", "coral")
timmy.speed(0)
my_screen = Screen()
timmy.begin_fill()

for n in range(12):
    for i in range(2):
        timmy.circle(100,45)
        timmy.circle(100//4,45)
        timmy.circle(100//4,45)
        timmy.circle(100//4,45)
    timmy.right(30)

timmy.end_fill()

my_screen.exitonclick()

