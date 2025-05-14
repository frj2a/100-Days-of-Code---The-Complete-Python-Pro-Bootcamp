from tkinter import *
import time

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 2 # 25
SHORT_BREAK_MIN = 1 # 5
LONG_BREAK_MIN = 2 # 20
SECS_IN_MIN = 10 # 60

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
phase = 0

# ---------------------------- TIMER RESET ------------------------------- #
def timer_reset():
    global time_start, time_end
    time_start = time.time_ns()
    time_end = time_start - 1

# ---------------------------- TIMER MECHANISM ------------------------------- #

def get_time():
    global time_end, time_start, phases, phase
    time_end = time.time_ns()
    time_now = (time_end - time_start) // 1_000_000_000
    minutes = (phases[phase]["time"] - 1) - (time_now // SECS_IN_MIN)
    seconds = SECS_IN_MIN - (time_now % SECS_IN_MIN) - 1
    if time_now == phases[phase]["time"] * SECS_IN_MIN - 0:
        phase += 1
        if phase % 8 == 0:
            title_label.config(fg=RED)
        elif phase % 2 == 0:
            title_label.config(fg=GREEN)
        else:
            title_label.config(fg=PINK)
        phase = phase % len(phases)
        title_label.config(text=phases[phase]["period"])
        timer_reset()
    return str(f"{minutes:02}:{seconds:02}"), phases[phase]["time"] * SECS_IN_MIN - time_now

def start_timer():
    title_label.config(text=phases[phase]["period"])
    count_down()

def end_timer():
    pass


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down():
    timer_reset()
    time_now = get_time()
    canvas.itemconfig(time_text, text="")
    canvas.itemconfig(time_text, text=time_now[0])
    print(time_now[1])
    window.after(1000, count_down)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.minsize(width=200, height=200)
window.config(padx=20, pady=20, bg=YELLOW)

title_label = Label(text="Timer", font=(FONT_NAME, 48, "bold"), fg=GREEN, bg=YELLOW)
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
time_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 32, "bold"))
canvas.grid(column=1, row=1)


button_start = Button(text="Start", command=start_timer, highlightthickness=0)
button_start.grid(column=0, row=2)

button_end = Button(text="Reset", command=end_timer, highlightthickness=0)
button_end.grid(column=2, row=2)

check_marks = Label(text="✓", font=(FONT_NAME, 16, "bold"), fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)



# while keep_going:
#     time.sleep(1)
#     print(get_time())

window.mainloop()
