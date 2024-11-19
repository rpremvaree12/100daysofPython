import colorgram
import turtle as t

tim = t.Turtle()
tim.speed("fastest")
t.colormode(255)
my_screen = t.Screen()
my_screen.setup(width=500,height=500)

rgb_colors = []
colors = colorgram.extract('hirst1.jpg',72)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb_colors.append((r,g,b))

def draw_circle(x,y,color):
    tim.penup()
    tim.goto(x,y)
    tim.pendown()
    tim.color(color)
    tim.fillcolor(color)
    tim.begin_fill()
    tim.circle(25)
    tim.end_fill()

# print(len(rgb_colors))
for y in range(6):
    for x in range(12):
        print(x+y*5)
        # draw_circle(-250+x*100, -250+y*100, rgb_colors[y+x*5])
my_screen.exitonclick()