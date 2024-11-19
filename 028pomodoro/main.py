from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#1B9C85"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
reps_checks = ""
rep_text = "Pomodoro"
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    rep_text = "Pomodoro"
    reps = 0
    reps_checks=""
    timer_label.config(text=rep_text)
    check_marks.config(text=reps_checks)
    
    
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps, rep_text
    reps += 1
    
    # if it's the 2,4,6 rep then take a short break
    # if it's the 8 rep take a long break
    if reps % 8 == 0:
        timer_label.config(fg=RED)
        rep_text = f"LONG BREAK Round {reps}"
        work_sec = LONG_BREAK_MIN * 60
    elif reps % 2 == 0:
        timer_label.config(fg=PINK)
        rep_text = f"SHORT BREAK Round {reps}"
        work_sec = SHORT_BREAK_MIN * 60
    else:
        rep_text = f"WORK Round {reps}"
        timer_label.config(fg=GREEN)
        work_sec = WORK_MIN * 60
    timer_label.config(text=rep_text)
    count_down(work_sec)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    # format the time
    minutes = count // 60
    seconds = count % 60

    # dynamic typing
    if seconds < 10:
        seconds = f"0{seconds}"

    # update the timer text
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        global rep_text, reps_checks
        if reps % 2 == 1:
            reps_checks += "✅"
        check_marks.config(text=reps_checks)
        start_timer()
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro Timer")
window.minsize(width=400, height=400)
window.config(padx=100, pady=50,bg=YELLOW)


canvas = Canvas(width=210, height=224,bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="./tomato.png")
canvas.create_image(105,112, image=tomato_img)

timer_label = Label(text=rep_text, bg=YELLOW, fg=GREEN, font=(FONT_NAME, 30, "bold"))
timer_label.grid(column=2,row=1)

timer_text = canvas.create_text(105,130,text="00:00", fill="white",font=(FONT_NAME,35,"bold"))
start_btn = Button(text="start", command=start_timer, highlightthickness=0)
start_btn.grid(column=1, row=3)

reset_btn = Button(text="reset", command=reset, highlightthickness=0, bg=YELLOW, borderwidth=0)
reset_btn.grid(column=3, row=3)

check_marks = Label(text=reps_checks, fg=GREEN, bg=YELLOW)
check_marks.grid(column=2,row=4)

canvas.grid(column=2, row=2)






window.mainloop()