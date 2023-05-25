###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
import colorgram
import turtle as t

tim = t.Turtle()
tim.speed("fastest")
t.colormode(255)
my_screen = t.Screen()

rgb_colors = []
colors = colorgram.extract('hirst1.jpg', 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb_colors.append((r,g,b))

def draw_circle(x,y,color):
    tim.penup()
    tim.goto(x,y)
    tim.pendown()
    tim.fillcolor(color)
    tim.begin_fill()
    tim.circle(50)
    tim.end_fill()

draw_circle(0,0,(255,0,0))

for x in range(6):
    for y in range(5):
        print(x*5 + y)
        draw_circle(x, y, rgb_colors[y + x*5])

my_screen.exitonclick()