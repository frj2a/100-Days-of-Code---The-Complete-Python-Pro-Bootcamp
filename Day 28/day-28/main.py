from tkinter import *
import time

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
SECS_IN_MIN = 60

time_start = time.time_ns()
time_end = time_start
keep_going = True
phases = {
    0: { "time":WORK_MIN, "period":"Work"},
    1: { "time":SHORT_BREAK_MIN, "period": "Break"},
    2: { "time":WORK_MIN,"period":"Work"},
    3: { "time":SHORT_BREAK_MIN, "period": "Break"},
    4: { "time":WORK_MIN,"period":"Work"},
    5: { "time":SHORT_BREAK_MIN, "period": "Break"},
    6: { "time":WORK_MIN,"period":"Work"},
    7: { "time":LONG_BREAK_MIN, "period": "Long Break"},
}
phase = len(phases)
timer = None

# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    check_marks.config(text="")
    global phase
    phase = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global phase
    phase += 1
    if phase >= len(phases):
        phase = 0

    if phases[phase]["time"] == LONG_BREAK_MIN:
        title_label.config(text="Break", fg=RED)
    elif phases[phase]["time"] == SHORT_BREAK_MIN:
        title_label.config(text="Break", fg=PINK)
    else:
        title_label.config(text="Work", fg=GREEN)

    count_down(phases[phase]["time"] * SECS_IN_MIN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):

    count_min = count // SECS_IN_MIN
    count_sec = count % SECS_IN_MIN

    canvas.itemconfig(timer_text, text=f"{count_min:02}:{count_sec:02}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = phase//2
        for _ in range(work_sessions):
            marks += "✓"
        check_marks.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

check_marks = Label(fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)






window.mainloop()











