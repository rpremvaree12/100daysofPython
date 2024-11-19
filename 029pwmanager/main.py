from tkinter import *
from tkinter import messagebox
import pyperclip as clip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():

    # write random password generator
    random_password = "asfkasjfl923"
    password_input.delete(0,END)
    password_input.insert(0,random_password)
    clip.copy(random_password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Missing Info", message="There's missing information.")
    else:
        is_ok = messagebox.askokcancel(title="Add info?", message=f"These are the details entered:\n website: {website}\nemail: {email}\npassword: {password}\nOkay to add?")
    # add to file - "a" append, create the file if doesn't exist
    if is_ok:
        with open("pw_manager_data.txt","a") as file:
            file.write(f"{website}:{email}:{password}\n")
            website_input.delete(0,'end')
            email_input.delete(0,'end')
            email_input.insert(0,"@gmail.com")
            password_input.delete(0,"end")
            
        
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password manager")
window.config(padx=20,pady=20)
canvas = Canvas(height=200,width=200)
lock_img = PhotoImage(file="./logo.png")
logo = canvas.create_image(100,100,image=lock_img)
canvas.grid(column=1,row=0)

website_label = Label(text="Website",anchor="e")
website_label.grid(column=0,row=1)

website_input = Entry(width=52)
website_input.grid(column=1, row=1,columnspan=2)

email_label = Label(text="Email/Username",justify="right")
email_label.grid(column=0, row=2)

email_input = Entry(width=52)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0,"@gmail.com")

password_label = Label(text="Password",justify="right")
password_label.grid(column=0, row=3)

password_input = Entry(width=34)
password_input.grid(column=1,row=3)
generate_pw_btn = Button(text="Generate Password", command=generate, justify="right")
generate_pw_btn.grid(column=2,row=3)

add_info_btn = Button(text="Add Info",width=50,command=save_password)
add_info_btn.grid(column=1,row=4, columnspan=2)


window.mainloop()