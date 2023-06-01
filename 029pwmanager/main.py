from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password manager")
window.config(padx=20,pady=20)
canvas = Canvas(height=200,width=200)
lock_img = PhotoImage(file="./logo.png")
logo = canvas.create_image(100,100,image=lock_img)
canvas.grid(column=2,row=1)

website_label = Label(text="Website")
website_label.grid(column=1,row=2)

website_input = Entry(width=50)
website_input.grid(column=2, row=2)

email_label = Label(text="Email/Username")
email_label.grid(column=1, row=3)

email_input = Entry(width=50)
email_input.grid(column=2, row=3)

password_label = Label(text="Password")
password_label.grid(column=1, row=4)

password_input = Entry(width=50)
password_input.grid(column=2,row=4)

generate_pw_btn = Button(text="Generate Password")
generate_pw_btn.grid(column=3,row=4)

add_info_btn = Button(text="Add Info")
add_info_btn.grid(column=2,row=5)


window.mainloop()