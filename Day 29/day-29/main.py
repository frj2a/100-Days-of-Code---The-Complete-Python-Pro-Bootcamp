from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# https://tkdocs.com/tutorial/canvas.html
# https://tkdocs.com/tutorial/widgets.html#entry
# https://pypi.org/project/pyperclip/

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Arial"
FILE_NAME = "data.txt"
REGULAR_USER = "frj2a@yahoo.com"

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_passwd():
    # parts from Day 5

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]
    password_list = password_letters + password_symbols + password_numbers

    # password_list = []
    #
    # for char in range(nr_letters):
    #     password_list += random.choice(letters)
    #
    # for char in range(nr_symbols):
    #     password_list += random.choice(symbols)
    #
    # for char in range(nr_numbers):
    #     password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = "".join(password_list)

    # password = ""
    # for char in password_list:
    #     password += char

    pwd_input.delete(0, END)
    pwd_input.insert(0, password)

    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_pwd():
    site = site_input.get()
    user = usr_input.get()
    pwd = pwd_input.get()

    if len(site)==0 or len(user)==0 or len(pwd)==0:
        messagebox.askokcancel(title="Oops!", message="Don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=site, message=f"These are the details entered:\nEmail: {user}\n"
                                                           f"Password: {pwd}\nIs it ok to save?")
        if is_ok:
            site_input.delete(0, END)
            usr_input.delete(0, END)
            usr_input.insert(0, REGULAR_USER)
            pwd_input.delete(0, END)
            with open(FILE_NAME, "a") as data_file:
                data_file.write(f"{site},{user},{pwd}\n")

# ---------------------------- UI SETUP ------------------------------- #

try:
    with open(FILE_NAME, "r") as file:
        contents = file.readlines()
except:
    with open(FILE_NAME, "w") as file:
        file.write("site,user,password\n")

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")

canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

site_label = Label(text="Website:", fg="black", bg="white") # , font=(FONT_NAME, 16))
site_label.grid(column=0, row=1, sticky='e')

usr_label = Label(text="Email/Username:",  fg="black", bg="white") # , font=(FONT_NAME, 16))
usr_label.grid(column=0, row=2, sticky='e')

passwd_label = Label(text="Password:", fg="black", bg="white") # , font=(FONT_NAME, 16))
passwd_label.grid(column=0, row=3, sticky='e')

site_input = Entry(width=35, fg="black", bg="white") # , font=(FONT_NAME, 20))
site_input.grid(column=1, row=1, columnspan=2, sticky='ew')
site_input.get()
site_input.focus()

usr_input = Entry(width=35, fg="black", bg="white") # , font=(FONT_NAME, 20))
usr_input.grid(column=1, row=2, columnspan=2, sticky='ew')
usr_input.insert(0, REGULAR_USER)
usr_input.get()

pwd_input = Entry(width=21, fg="black", bg="white") # , font=(FONT_NAME, 20))
pwd_input.grid(column=1, row=3, sticky='ew')
pwd_input.get()

generate_button = Button(text="Generate Password", command=generate_passwd, fg="black", bg="lightgray", highlightthickness=0) # , font=(FONT_NAME, 16))
generate_button.grid(column=2, row=3)

save_button = Button(text="Add", width=36, command=save_pwd, fg="black", bg="lightgray", highlightthickness=0) # , font=(FONT_NAME, 16))
save_button.grid(column=1, row=4, columnspan=2, sticky='we')

window.mainloop()
