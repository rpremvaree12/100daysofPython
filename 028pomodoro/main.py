from tkinter import *
import time
import datetime
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 
start_btn = Button(text="start")
reset_btn = Button(text="reset")
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def countdown(h,m,s):
    total_seconds = h * 3600 + m * 60 + s * 60
    while total_seconds > 0:
        timer = datetime.timedelta(seconds= total_seconds)
        print(timer)
        time.sleep(1)
        total_seconds -= 1
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro Technique")
# window.minsize(width=400, height=400)
window.config(padx=100, pady=50,bg=YELLOW)

canvas = Canvas(width=210, height=224,bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="./tomato.png")
canvas.create_image(105,112, image=tomato_img)
canvas.create_text(105,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))

canvas.pack()






window.mainloop()