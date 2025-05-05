import turtle

# tim = turtle.Turtle()
screen = turtle.Screen()

turtle.colormode(255)

# def move_forward():
#     tim.forward(10)
#
# def move_backward():
#     tim.backward(10)
#
# def turn_left():
#     tim.setheading(tim.heading() + 10)
#
# def turn_right():
#     tim.setheading(tim.heading() - 10)
#
# def clear_screen():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()
#
# screen.listen()
# screen.onkey(fun=move_forward, key="w")
# screen.onkey(fun=move_backward, key="s")
# screen.onkey(fun=turn_left, key="a")
# screen.onkey(fun=turn_right, key="d")
# screen.onkey(fun=clear_screen, key="c")

import random

colors = ["red", "yellow", "blue", "green", "orange", "violet", "purple"]
tims = []
is_race_on = False

screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race?  Enter a color:")

for color in colors:
    tim = turtle.Turtle()
    tim.penup()
    tim.goto(x=int(-screen.window_width() / 2) + 20,
             y=int(screen.window_height() / (len(colors)+1) * (len(tims) + 1) ) - screen.window_height() / 2)
    # tim.pendown()
    tim.color(color)
    tim.shape("turtle")
    tims.append(tim)

if user_bet:
    is_race_on = True

while is_race_on:
    for tim in tims:
        if tim.xcor() > int(screen.window_width() / 2):
            winning_color = tim.pencolor()
            if winning_color == user_bet:
                print("You've won!")
            else:
                print("You've lost!")
            print(f"The {winning_color} turtle is the winner.")
            is_race_on = False
        rand_dist = random.randint(0, 10)
        tim.forward(rand_dist)

screen.exitonclick()