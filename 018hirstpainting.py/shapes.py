import turtle as t


tim = t.Turtle()
tim.pensize(5)

for i in range(3,10):
    for _ in range(i):
        tim.forward(100)
        tim.right(360/i)

screen = t.Screen()
screen.exitonclick()