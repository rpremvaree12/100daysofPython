from tkinter import *

window = Tk()
window.title("Mile Converter!")
window.minsize(height=100, width=300)
# window padding
window.config(padx=20, pady=20)

def converter():
    miles = float(input_box.get())
    km_result.config(text=round(miles * 1.609,2))


input_box = Entry(width=10)
input_box.insert(END, string="0")
input_box.grid(column=2,row=1)

miles_label = Label(text="miles", width=20)
miles_label.config()
miles_label.grid(column=3,row=1)

is_equal_label = Label(text="is equal to ", width=20)
is_equal_label.grid(column=1, row=2)

km_result = Label(text="0", width=20)
km_result.grid(column=2, row=2)

km_label = Label(text="kilometers.", width=20)
km_label.grid(column=3, row=2)

convert_btn = Button(text="Convert!", command=converter)
convert_btn.grid(column=2, row=3)

window.mainloop()