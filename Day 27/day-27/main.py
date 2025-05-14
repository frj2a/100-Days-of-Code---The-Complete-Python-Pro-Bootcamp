# import tkinter
#
# window = tkinter.Tk()
# window.title("My First GUI Program")
# window.minsize(width=500, height=300)
#
# # Label
# my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))
#
# # https://docs.python.org/3/library/tkinter.html#the-packer
# #my_label.pack(side="left", expand=True) # this centers the label
# my_label.pack() # this centers the label
#
#
# my_label["text"] = "New Text"
# my_label.config(text="Yet Another Text")
#
#
# # Button
#
# def button_clicked():
#     # global my_label
#     # print("I got clicked")
#     # my_label.config(text="Button Got Clicked")
#     new_text = input_field.get()
#     my_label.config(text=new_text)
#
# button = tkinter.Button(text="Click Me", command=button_clicked)
# button.pack()
#
#
# # Entry
#
# input_field = tkinter.Entry(width=10)
# input_field.pack()
#
#
#
#
#
#
# window.mainloop()


from tkinter import *


def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)


window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

#Label
my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)

#Button
button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

new_button = Button(text="New Button")
new_button.grid(column=2, row=0)

#Entry
input = Entry(width=10)
print(input.get())
input.grid(column=3, row=2)


window.mainloop()
