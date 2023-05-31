import tkinter

# Tk class
window = tkinter.Tk()
window.title("first GUI program")
window.minsize(width=500, height=300)

# Label class
my_label = tkinter.Label(text="I am a label", font=("Arial",16,"bold"))
# place the label - in the center by default
my_label.config(text="new label")
my_label.pack(side="right")


# button presses
def buttton_pressed():
   value = my_entry.get()
   my_label.config(text=value)

my_button = tkinter.Button(text="click me!", command=buttton_pressed)
my_button.pack(side="right")

# entry

my_entry = tkinter.Entry(width=10)
my_entry.pack(side="bottom")

# text
my_text = tkinter.Text(height=5, width =3)

# scale

# spinbox

# checkbutton

# radiobutton

# list box

# layout managers
# pack
# place - precise positioning with x and y
# top left is 0,0
# grid - name column and row number
# relative to other widgets





# keep window open and listen
# keep all instructions between these two commands
window.mainloop()