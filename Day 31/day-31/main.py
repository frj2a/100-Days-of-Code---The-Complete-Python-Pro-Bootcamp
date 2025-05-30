
import pandas
import random
from tkinter import *
from tkinter import messagebox
import random
# import pyperclip

BACKGROUND_COLOR = "#B1DDC6"

flip_timer = ""

try:
    data = pandas.read_csv("data/french_words_person.csv")

except FileNotFoundError:
    try:
        data = pandas.read_csv("data/french_words.csv")
    except FileNotFoundError:
        print("French to English data file doesn't exist in 'data' directory.")
        exit(0)

# data_map = {row.French: row.English for (index, row) in data.iterrows()}

data_dict = data.to_dict(orient="records")
current_card = random.choice(data_dict)

def flip_card():
    canvas.itemconfig(canvas_image, image=card_back_img)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")

def new_card():
    global current_card, flip_timer
    if flip_timer != "":
        window.after_cancel(flip_timer)
    current_card = random.choice(data_dict)
    canvas.itemconfig(canvas_image, image=card_front_img)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    flip_timer = window.after(3000, func=flip_card)

def right_pressed():
    if len(data_dict) > 0:
        data_dict.remove(current_card)
    new_data = pandas.DataFrame(data_dict)
    new_data.to_csv("data/french_words_person.csv", index=False)
    new_card()

def wrong_pressed():
    new_card()


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="Language", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)



# Buttons
right_img = PhotoImage(file="images/right.png")
button_right = Button(image=right_img, highlightthickness=0, text="", command=right_pressed, bg=BACKGROUND_COLOR)
button_right.grid(row=1, column=1)

wrong_img = PhotoImage(file="images/wrong.png")
button_wrong = Button(image=wrong_img, highlightthickness=0, text="", command=wrong_pressed, bg=BACKGROUND_COLOR)
button_wrong.grid(row=1, column=0)

right_pressed()

window.mainloop()
