import turtle
import pandas as pd

# Game set up
screen = turtle.Screen()
screen.title("US State Map Game")

# Load map onto turtle screen
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# get coordinates of states rel to map image (already in 50_states.csv)
def get_mouse_click_cor(x,y):
    print(x,y)
# event listener to call x and y coordinates
turtle.onscreenclick(get_mouse_click_cor)

# keeps screen open even if clicked
# turtle.mainloop()


# Game data set up
state_df = pd.read_csv("50_states.csv")
state_names = state_df["state"].to_list()


states_found = []
states_count = 0
game_on = True
t = turtle.Turtle()
t.penup()
t.hideturtle()
t.speed(0)
t.color("blue")

while game_on:
    answer_state = screen.textinput(title="Guess a state", prompt="What's another state? ").capitalize()
    print(states_count)
    if answer_state in state_names and answer_state not in states_found:
        states_count += 1
        states_found.append(answer_state)
        state_data = state_df[state_df.state==answer_state]
        t.goto(int(state_data.x.iloc[0]),int(state_data.y.iloc[0]))
        t.write(answer_state,font=("Arial", 12, "bold"))
    elif states_count >= 50 or answer_state == "End":
        game_on = False
    else:
        print("Not a state. Try again.")


if states_count >= 50:
    t.color("red")
    t.goto(0,0)
    t.write("You found them all!")
screen.exitonclick()

