import pandas
import turtle

FONT = ("Arial", 8, "normal")

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.setup(725,491, 100, 100)

text_turtle = turtle.Turtle()
text_turtle.penup()
text_turtle.hideturtle()
text_turtle.speed("fastest")

data = pandas.read_csv("50_states.csv")
state_count = data.state.count()
states = data["state"].to_list()
guesses = []
while len(guesses) < state_count:
    answer_state = screen.textinput(title=f"{len(guesses) }/{state_count} States Correct", prompt="What's another state's name?")
    if answer_state:
        answer_state = answer_state.title()
        # print (answer_state)
        # print(data["state"])
        if answer_state in states:
            if guesses.count(answer_state) == 0:
                guesses.append(answer_state)
                state_data = data[data.state == answer_state]
                text_turtle.goto(state_data.x.item(), state_data.y.item())
                text_turtle.write(state_data.state.item(), align="center", font=FONT)
    else:
        missing_states = []
        for state in states:
            if state not in guesses:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break


# turtle.mainloop()
# screen.exitonclick()
