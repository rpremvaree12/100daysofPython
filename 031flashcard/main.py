from tkinter import *
import pandas as pd
import random
BACKGROUND_COLOR = "#B1DDC6"


# 2. Create new flash cards
df = pd.read_csv("./data/french_words.csv")
data = df.to_dict(orient="records")

def new_word():
    global word, flip_timer
    word = random.choice(data)
    window.after_cancel(flip_timer)
    fr_word = word["French"]
    canvas.itemconfig(title_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=fr_word, fill="black")
    canvas.itemconfig(card, image=front_img)

    #Flip the cards
    flip_timer = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(card, image=back_img)
    en_word = word["English"]
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=en_word, fill="white")


# 1. Create UI
window = Tk()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# images
canvas = Canvas(width=800, height=526)

front_img = PhotoImage(file="./images/card_front.png")
back_img = PhotoImage(file="./images/card_back.png")

card = canvas.create_image(400, 263, image=front_img)
title_text = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"), fill="black")
word_text = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"), fill="black")
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)

canvas.grid(column=0,row=0, columnspan=2)


wrong_img = PhotoImage(file="./images/wrong.png")
wrong_btn = Button(image=wrong_img, bd=0, command=new_word, highlightthickness=0)
wrong_btn.grid(column=0,row=1)

right_img = PhotoImage(file="./images/right.png")
right_btn = Button(image=right_img, bd=0, command=new_word, highlightthickness=0)
right_btn.grid(column=1,row=1)



# 3. Flip the cards
flip_timer = window.after(3000, flip_card)
new_word()
# 4. Save the progress

window.mainloop()