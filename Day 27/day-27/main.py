import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Label
my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))

# https://docs.python.org/3/library/tkinter.html#the-packer
#my_label.pack(side="left", expand=True) # this centers the label
my_label.pack() # this centers the label


my_label["text"] = "New Text"
my_label.config(text="Yet Another Text")


# Button

def button_clicked():
    # global my_label
    # print("I got clicked")
    # my_label.config(text="Button Got Clicked")
    new_text = input_field.get()
    my_label.config(text=new_text)

button = tkinter.Button(text="Click Me", command=button_clicked)
button.pack()


# Entry

input_field = tkinter.Entry(width=10)
input_field.pack()






window.mainloop()