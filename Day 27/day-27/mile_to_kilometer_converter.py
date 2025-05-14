from tkinter import *

 # 186.41182099494202 miles = 300 kilometers
def miles_to_kilometers():
    miles = float(input.get())
    label_result.config(text=str(miles*1.60934))


window = Tk()
window.title("My First GUI Program")
# window.minsize(width=100, height=50)
window.config(padx=10, pady=10)

FONT = ("Arial", 12, "bold")

#Labels
label_1 = Label(text="is equal to", font=FONT)
label_1.grid(column=0, row=1)
#label_1.config(padx=20, pady=20)

label_2 = Label(text="miles", font=FONT)
label_2.grid(column=2, row=0)
#label_2.config(padx=20, pady=20)

label_3 = Label(text="km", font=FONT)
label_3.grid(column=2, row=1)
#label_3.config(padx=20, pady=20)

label_result = Label(text="0", font=FONT)
label_result.grid(column=1, row=1)
#label_3.config(padx=20, pady=20)


#Button
button = Button(text="Calculate", command=miles_to_kilometers)
button.grid(column=1, row=2)
#button.config(padx=20, pady=20)


#Entry
input = Entry(width=18)
input.get()
input.grid(column=1, row=0)


window.mainloop()
